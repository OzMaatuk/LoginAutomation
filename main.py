from configparser import Error as ConfigParserError 
import logging
import sys
from config import AppConfig

from driver import PlaywrightDriver
from logger import configure_application_logging
from login_automation.login.factory import FactoryLogin

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting main application.")
        cnf = AppConfig('config.ini')
        configure_application_logging(cnf.log_level, cnf.log_file, cnf.logging_format)

        # Use context manager for driver
        with PlaywrightDriver(cnf.headless, cnf.timeout) as driver:
            if not driver.page:
                raise Exception("Failed to initialize browser page")
                
            app = FactoryLogin.create_login('linkedin', driver.page)

            # Execute
            app.login(cnf.username, cnf.password)

    except ConfigParserError as e:
        logger.error(f"Error reading configuration: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()