# src/login/login.py

import logging
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from src.constants.constants import Constants


logger = logging.getLogger(__name__)

class Login:
    """Manages general login process."""

    def __init__(self, page: Page, constants: Constants):
        logger.info("Initializing Login instance")
        logger.debug(f"page: {page}, constants: {constants}")
        self.page = page
        self.constants = constants

    def login(self, username: str, password: str):
        logger.info("Starting login() method in Login class")
        logger.debug(f"username: {username}")
        login_url = self.constants.LOGIN_URL
        feed_url = self.constants.FEED_URL
        logger.debug(f"login_url: {login_url}, feed_url: {feed_url}")
        
        if login_url is None or feed_url is None:
            error_msg = "URL is not set in constants"
            logger.error(error_msg)
            raise Exception(error_msg)
        
        try:
            self.page.goto(login_url)
            self.page.wait_for_url(login_url)
            logger.info(f"Navigated to {login_url}")
        except PlaywrightTimeoutError as e:
            if feed_url in self.page.url:
                logger.info("Already logged in.")
                return

        if not self.validate_constants():
            raise Exception("Constants missing required attributes")
        locators_class = self.constants.Locators

        try:
            logger.info("Proceeding with login form submission.")
            logger.info("Not logged in, performing login.")
            
            USERNAME_TEXTFIELD = getattr(locators_class, "USERNAME_TEXTFIELD")
            PASSWORD_TEXTFIELD = getattr(locators_class, "PASSWORD_TEXTFIELD")
            LOGIN_BUTTON = getattr(locators_class, "LOGIN_BUTTON")

            self.page.fill(USERNAME_TEXTFIELD, username)
            
            if locators_class.NEXT_BUTTON:
                self.page.click(locators_class.NEXT_BUTTON)
                self.page.wait_for_selector(PASSWORD_TEXTFIELD)
            
            self.page.fill(PASSWORD_TEXTFIELD, password)
            self.page.click(LOGIN_BUTTON)
            self.page.wait_for_url(feed_url)
        except PlaywrightTimeoutError as e:
            raise Exception(f"Timeout waiting for feed url, login fails due to: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred during login: {e}")
            
    def validate_constants(self):
        # Check Locators exists and has Login
        locators_class = getattr(self.constants, 'Locators', None)
        if not locators_class:
            return False

        # Check Login attributes
        login_attrs = ['USERNAME_TEXTFIELD', 'PASSWORD_TEXTFIELD', 'LOGIN_BUTTON']
        return all(attr in locators_class.__dict__ for attr in login_attrs)