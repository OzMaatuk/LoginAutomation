# src/constants/constants.py

class Constants():

    def __init__(self):
            pass

    # --- Site ---
    BASE_URL = None
    LOGIN_URL = None
    FEED_URL = None

    # --- Driver ---
    DEFAULT_TIMEOUT = 12000
    DEFAULT_HEADLESS = True

    # --- Logging ---
    DEFAULT_LOGGING_LEVEL = "DEBUG"
    DEFAULT_LOGGING_FILE = "logs/main.log"
    DEFAULT_LOGGING_FORMAT = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'

    # Supported platforms
    SUPPORTED_PLATFORMS = {
        # Add more platforms here as needed in the ConstantsFacebook class init. 
        # 'facebook': {
        #     'login_class': LoginFacebook,
        #     'constants_class': ConstantsFacebook
        # },
    }

    # --- Locators ---
    class Locators:

        # --- REQUIERED Login Locators ---            
        USERNAME_TEXTFIELD = None
        PASSWORD_TEXTFIELD = None
        LOGIN_BUTTON = None
        NEXT_BUTTON = None

        def __init__(self):
            raise NotImplementedError("Abstarct Constants class does not have Locators implementation.")
