# src/constants/indeed.py

from login_automation.constants.constants import Constants

class ConstantsIndeed(Constants):

    def __init__(self):
        super().__init__()
        # Constants.SUPPORTED_PLATFORMS.update({
        #     'indeed': {
        #         'login_class': 'login_automation.login.indeed.LoginIndeed',
        #         'constants_class': 'login_automation.constants.indeed.ConstantsIndeed'
        #     }
        # })
        
    # --- Indeed URLs ---
    BASE_URL = "https://www.indeed.com"
    LOGIN_URL = f"https://secure.indeed.com/auth?"
    FEED_URL = f"{BASE_URL}/jobs?"

    # --- Locators ---
    class Locators(Constants.Locators):
        def __init__(self):
            pass

        # --- Indeed Login Locators ---            
        USERNAME_TEXTFIELD = "input#__email"
        PASSWORD_TEXTFIELD = "input#password"
        LOGIN_BUTTON = "button[type='submit']"