from configparser import Error as ConfigParserError 
import logging
from config import AppConfig

from driver import PlaywrightDriver
from logger import configure_application_logging

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting main application.")
        app_config = AppConfig('config.ini')
        configure_application_logging(app_config.log_level, app_config.log_file, app_config.logging_format)

        # Load user details

        # Load job URLs


        # Use context manager for driver
        with PlaywrightDriver(app_config.headless, app_config.timeout) as driver:
            if not driver.page:
                raise Exception("Failed to initialize browser page")
                
            app = Login()

            # Execute

    except ConfigParserError as e:
        logger.error(f"Error reading configuration: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()