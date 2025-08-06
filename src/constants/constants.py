# src/constants/constants.py


class Constants():

    # --- Driver ---
    DEFAULT_TIMEOUT = 12000
    DEFAULT_HEADLESS = True

    # --- Logging ---
    DEFAULT_LOGGING_LEVEL = "DEBUG"
    DEFAULT_LOGGING_FILE = "logs/main.log"
    DEFAULT_LOGGING_FORMAT = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'

    # Supported platforms
    SUPPORTED_PLATFORMS = {
        'linkedin': {
            'login_class': LoginLinkedIn,
            'constants_class': ConstantsLinkedIn
        },
        # Add more platforms here as needed
        # 'facebook': {
        #     'login_class': LoginFacebook,
        #     'constants_class': ConstantsFacebook
        # },
    }
    # --- Locators ---
    class Locators:
        def __init__(self):
            raise NotImplementedError("Abstarct Constants class does not have Locators implementation.")
