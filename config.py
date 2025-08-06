import configparser
from src.constants.constants import (
    DEFAULT_HEADLESS,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_FILE,
    DEFAULT_TIMEOUT,
    SUPPORTED_PLATFORMS
)
from src.constants.linkedin import ConstantsLinkedIn


class AppConfig:
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.load_configurations()

    def load_configurations(self):
        cfg = self.config
        self.logging_format = cfg['logging'].get('logging_format', DEFAULT_LOG_FORMAT, raw=True)
        self.log_level = cfg['logging'].get('log_level', DEFAULT_LOG_LEVEL)
        self.log_file = cfg['logging'].get('log_file', DEFAULT_LOG_FILE)
        self.timeout = cfg['driver'].getint('timeout', DEFAULT_TIMEOUT)
        self.headless = cfg['driver'].getboolean('headless', DEFAULT_HEADLESS)

        # Load Credentials: (First from .env, else from config)
        self.username = os.environ.get("USERNAME")
        if not self.username:
            self.username = config.get("user_info", "username", fallback="username")
            if not self.username:
                raise ValueError("USERNAME is not set in environment variables or config.ini.")

        self.password = os.environ.get("PASSWORD")
        if not self.password:
            self.password = config.get("user_info", "password", fallback="password")
            if not self.password:
                raise ValueError("PASSWORD is not set in environment variables or config.ini.")

        site_type = config.get("general", "site_type", fallback=None)
        self.login_url = None
        if not site_type:
            raise ValueError("site_type is not set in config.ini.")
        supported_sites = SUPPORTED_PLATFORMS.keys()
        if site_type not in supported_sites:
            logger.warning(f"site_type in config.ini is not supported. supported sites are {supported_sites}.")
            logger.warning(f"try login to unsupported site.")
            self.login_url = config.get("general", "login_url", fallback=None)
            if not self.login_url:
                raise raise ValueError("login_url is not configured in config.ini, it requiered due to not supported site_type.")
        elif (site_type == "linkedin"):
            self.login_url = ConstantsLinkedIn.LOGIN_URL
            self.feed_url = ConstantsLinkedIn.FEED_URL
        else:
            raise raise ValueError("login_url is not provided, you should set supported site_type, or provide login_url in config.ini")