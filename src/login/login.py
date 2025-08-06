# src/login/login.py

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
import logging
from src.exceptions import LoginError
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
            raise LoginError(error_msg)
        
        try:
            self.page.goto(login_url)
            self.page.wait_for_url(login_url)
            logger.info(f"Navigated to {login_url}")
        except PlaywrightTimeoutError as e:
            if feed_url in self.page.url:
                logger.info("Already logged in.")
                return

        if not self.validate_constants():
            raise LoginError("Constants missing required attributes")
        login_class = getattr(self.constants.Locators, "Login")

        try:
            logger.info("Proceeding with login form submission.")
            logger.info("Not logged in, performing login.")
            
            self.page.fill(login_class.USERNAME_FIELD, username)
            
            if login_class.NEXT_BUTTON:
                self.page.click(login_class.NEXT_BUTTON)
                self.page.wait_for_selector(login_class.PASSWORD_FIELD)
            
            self.page.fill(login_class.PASSWORD_FIELD, password)
            self.page.click(login_class.LOGIN_BUTTON)
            self.page.wait_for_url(feed_url)
        except Exception as e:
            raise LoginError(f"An unexpected error occurred during login: {e}")
            
    def validate_constants(self):
        # Check Locators exists and has Login
        locators_class = getattr(self.constants, 'Locators', None)
        if not locators_class
            return False

        # Check Login attributes
        login_attrs = ['USERNAME_LOCATOR', 'PASSWORD_LOCATOR', 'LOGIN_BUTTON_LOCATOR']
        return all(attr in locators_class.Login.__dict__ for attr in login_attrs)