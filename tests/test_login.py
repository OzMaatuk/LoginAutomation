# tests\test_login.py

import configparser
import os
import pytest
import pytest_mock
import logging
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from src.login.login import Login
from src.exceptions import LoginError
from src.constants.linkedin import ConstantsLinkedIn
Locators = ConstantsLinkedIn.Locators

logger = logging.getLogger(__name__)

class TestLogin:

    def test_successful_login(self, playwright_page_no_data: Page, username: str, password: str) -> None:
        """Tests successful login using pytest-mock."""
        logger.info("Testing successful login scenario")

        login_manager = Login(playwright_page_no_data, ConstantsLinkedIn())
        login_manager.login(username, password)

        assert playwright_page_no_data.url == ConstantsLinkedIn.FEED_URL

    def test_login_timeout(self, mocker: pytest_mock.MockFixture, playwright_page_no_data: Page, username: str, password: str) -> None:
        """Tests the timeout scenario during login."""
        logger.info("Testing login timeout scenario")

        mocker.patch.object(
            playwright_page_no_data, 
            'wait_for_url',
            side_effect=PlaywrightTimeoutError("Timeout")
        )

        login_manager = Login(playwright_page_no_data, ConstantsLinkedIn())

        with pytest.raises(LoginError, match="Login failed Due to timeout."):
            login_manager.login(username, password)

    def test_login_unexpected_error(self, mocker: pytest_mock.MockFixture, playwright_page_no_data: Page, username: str, password: str) -> None:
        """Tests for unexpected errors during login."""
        logger.info("Testing unexpected error scenario during login")

        mocker.patch.object(
            playwright_page_no_data, 
            'wait_for_url',
            side_effect=Exception("Test Unexpected Error")
        )

        login_manager = Login(playwright_page_no_data, ConstantsLinkedIn())

        with pytest.raises(LoginError, match=r"An unexpected error occurred during login: Test Unexpected Error"):
            login_manager.login(username, password)

    def test_invalid_credentials(self, playwright_page_no_data: Page, config: configparser.ConfigParser) -> None:
        """Tests the invalid credentials scenario during login."""
        logger.info("Testing invalid credentials scenario during login")

        invalid_username = config.get("invalid_credentials", "username")
        invalid_password = config.get("invalid_credentials", "password")

        login_manager = Login(playwright_page_no_data, ConstantsLinkedIn())

        with pytest.raises(LoginError, match="Login failed Due to timeout."):
            login_manager.login(invalid_username, invalid_password)
