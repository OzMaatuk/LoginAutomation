# src/constants/linkedin.py

from src.constants.constants import Constants

class ConstantsLinkedIn(Constants):

    # --- LinkedIn URLs ---
    BASE_URL = "https://www.linkedin.com"
    LOGIN_URL = f"{BASE_URL}/login"
    FEED_URL = f"{BASE_URL}/feed/"

    # --- Locators ---
    class Locators(Constants.Locators):
        def __init__(self):
            pass

        # --- LinkedIn Login Locators ---            
        USERNAME_LOCATOR = "input#username"
        PASSWORD_LOCATOR = "input#password"
        LOGIN_BUTTON_LOCATOR = "button[data-litms-control-urn='login-submit']"