# src/constants/linkedin.py

from login_automation.constants.constants import Constants

class ConstantsLinkedIn(Constants):

    def __init__(self):
        super().__init__()
        # Constants.SUPPORTED_PLATFORMS.update({
        #     'linkedin': {
        #         'login_class': 'login_automation.login.linkedin.LoginLinkedIn',
        #         'constants_class': 'login_automation.constants.linkedin.ConstantsLinkedIn'
        #     }
        # })
        
    # --- LinkedIn URLs ---
    BASE_URL = "https://www.linkedin.com"
    LOGIN_URL = f"{BASE_URL}/login"
    FEED_URL = f"{BASE_URL}/feed/"

    # --- Locators ---
    class Locators(Constants.Locators):
        def __init__(self):
            pass

        # --- LinkedIn Login Locators ---            
        USERNAME_TEXTFIELD = "input#username"
        PASSWORD_TEXTFIELD = "input#password"
        LOGIN_BUTTON = "button[data-litms-control-urn='login-submit']"