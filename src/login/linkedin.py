# src/login/linkedin.py

import logging
from playwright.sync_api import Page
from src.login.login import Login
from src.constants.linkedin import ConstantsLinkedIn


logger = logging.getLogger(__name__)

class LoginLinkedIn(Login):
    """Manages the login process for LinkedIn."""

    def __init__(self, page: Page, constants: ConstantsLinkedIn):
        logger.info("Initializing LoginLinkedIn instance")
        super().__init__(page, constants)

    def login(self, username: str, password: str):
        logger.info("Starting login() method in LoginLinkedIn class")
        super().login(username, password)