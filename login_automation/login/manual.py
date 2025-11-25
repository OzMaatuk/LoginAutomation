# login_automation/login/manual.py

import logging
from typing import Optional
from playwright.sync_api import Page
from login_automation.constants.constants import Constants
from login_automation.login.login import Login


logger = logging.getLogger(__name__)

class LoginManually(Login):
    """Manages the login process for LinkedIn."""

    def __init__(self, page: Page, constants : Optional[Constants]):
        logger.info("Initializing LoginManually instance")
        if not page:
            error_msg = "Page object is required"
            logger.error(error_msg)
            raise Exception(error_msg)
        self.page = page
        self.constants = constants
        
    def login(self, username: Optional[str], password: Optional[str]):
        logger.info("Starting login() method in LoginManually class")
        if self.constants:
            login_url = self.constants.LOGIN_URL
            feed_url = self.constants.FEED_URL
            logger.debug(f"login_url: {login_url}, feed_url: {feed_url}")
            
            try:
                self.page.goto(login_url)
                self.page.wait_for_url(login_url)
                logger.info(f"Navigated to {login_url}")
            except PlaywrightTimeoutError as e:
                if feed_url in self.page.url:
                    logger.info("Already logged in.")
                    return

        logger.info("You got 2 minutes to log in manually...")
        self.page.wait_for_event("load", timeout=120000)