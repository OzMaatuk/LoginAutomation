# login_automation/login/manual.py

import logging
from typing import Optional
from playwright.sync_api import Page
from login_automation.constants.constants import Constants
from login_automation.login.login import Login


logger = logging.getLogger(__name__)

class LoginManually(Login):
    """Manages the login process for LinkedIn."""

    def __init__(self, page: Page, constants : Optional[Constants] = None):
        logger.info("Initializing LoginManually instance")
        if not page:
            error_msg = "Page object is required"
            logger.error(error_msg)
            raise Exception(error_msg)
        self.page = page

    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        logger.info("Starting login() method in LoginManually class")
        logger.info("You got 2 minutes to log in manually...")
        self.page.wait_for_event("load", timeout=120000)