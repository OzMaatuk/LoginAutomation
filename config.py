import configparser
from src.constants import (
    DEFAULT_HEADLESS,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_FILE,
    DEFAULT_TIMEOUT
)

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