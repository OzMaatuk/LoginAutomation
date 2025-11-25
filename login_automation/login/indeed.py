# src/login/linkedin.py

import logging
from playwright.sync_api import Page
# from login_automation.login.login import Login
from login_automation.constants.linkedin import ConstantsIndeed
from login_automation.login.login import LoginManually

logger = logging.getLogger(__name__)

class LoginIndeed(LoginManually):
    """Manages the login process for Indeed."""

    def __init__(self, page: Page, constants: ConstantsIndeed):
        logger.info("Initializing LoginIndeed instance")
        super().__init__(page, constants)

    def login(self, username: Optional[str], password: Optional[str]):
        logger.info("Starting login() method in LoginIndeed class")
        super().login(username, password)