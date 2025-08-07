import configparser
import os
from login_automation.constants.constants import Constants
from login_automation.constants.linkedin import ConstantsLinkedIn


class AppConfig:
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.load_configurations()

    def load_configurations(self):
        cfg = self.config
        self.logging_format = cfg['logging'].get('logging_format', Constants.DEFAULT_LOGGING_FORMAT, raw=True)
        self.log_level = cfg['logging'].get('log_level', Constants.DEFAULT_LOGGING_LEVEL)
        self.log_file = cfg['logging'].get('log_file', Constants.DEFAULT_LOGGING_FILE)
        self.timeout = cfg['driver'].getint('timeout', Constants.DEFAULT_TIMEOUT)
        self.headless = cfg['driver'].getboolean('headless', Constants.DEFAULT_HEADLESS)

        # Load Credentials: (First from .env, else from config)
        self.username: str = os.environ.get("USERNAME", "")
        if self.username == "":
            self.username = cfg.get("user_info", "username", fallback="")
            if self.username == "":
                raise ValueError("USERNAME is not set in environment variables or config.ini.")

        self.password = os.environ.get("PASSWORD", "")
        if self.password == "":
            self.password = cfg.get("user_info", "password", fallback="password")
            if self.password == "":
                raise ValueError("PASSWORD is not set in environment variables or config.ini.")

        platform = cfg.get("general", "platform", fallback=None)
        self.login_url = None
        if not platform:
            raise ValueError("platform is not set in config.ini.")
        supported_platforms = Constants.SUPPORTED_PLATFORMS.keys()
        if platform not in supported_platforms:
            # logger.warning(f"platform in config.ini is not supported. supported sites are {supported_platforms}.")
            # logger.warning(f"try login to unsupported site.")
            self.login_url = cfg.get("general", "login_url", fallback=None)
            if not self.login_url:
                raise ValueError("login_url is not configured in config.ini, it requiered due to not supported platform.")
        elif (platform == "linkedin"):
            self.login_url = ConstantsLinkedIn.LOGIN_URL
            self.feed_url = ConstantsLinkedIn.FEED_URL
        else:
            raise ValueError("login_url is not provided, you should set supported platform, or provide login_url in config.ini")