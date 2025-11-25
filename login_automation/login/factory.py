# src/login/factory.py

import importlib
import logging
from typing import Union
from playwright.sync_api import Page
from login_automation.login.login import Login
from login_automation.constants.constants import Constants


logger = logging.getLogger(__name__)

class FactoryLogin:
    """Factory class for creating login instances based on platform type."""
    
    @classmethod
    def create_login(cls, platform: str, page: Page, constants: Union[Constants, None] = None) -> Login:
        """Create a login instance for the specified platform."""
        logger.info(f"Creating login instance for platform: {platform}")
        
        # If the platform is not supported raise a helpful error
        if not FactoryLogin.is_platform_supported(platform):
            supported = ', '.join(FactoryLogin.get_supported_platforms())
            error_msg = f"Platform '{platform}' is not supported. Supported platforms: {supported}"
            logger.error(error_msg)
            raise Exception(error_msg)
        
        try:
            platform_config = Constants.SUPPORTED_PLATFORMS[platform]
            
             # Dynamic import of classes from string paths
            login_class = cls._import_class(platform_config['login_class'])
            constants_class = cls._import_class(platform_config['constants_class'])
            
            
            # Use provided constants or create default ones. Some platforms use NoneType
            # (e.g. manual) as their constants class; handle that safely by leaving
            # constants as None when the constants_class is not instantiable.
            if constants is None:
                try:
                    logger.debug(f"No constants provided, creating default {constants_class.__name__} instance")
                    constants = constants_class()
                except Exception:
                    # If constants_class is types.NoneType or otherwise not callable
                    # just keep constants as None (some Login implementations accept None)
                    logger.debug("constants_class not instantiable, leaving constants as None")
            
            # Validate that constants are compatible
            if not isinstance(constants, constants_class):
                logger.warning(f"Constants type mismatch. Expected {constants_class.__name__}, got {type(constants).__name__}")
            
            logger.info(f"Creating {login_class.__name__} instance")
            return login_class(page, constants)
            
        except Exception as e:
            error_msg = f"Failed to create login instance for platform '{platform}': {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)
    
    @staticmethod
    def _import_class(class_path: str):
        """Dynamically import a class from a string path."""
        module_path, class_name = class_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    @staticmethod
    def get_supported_platforms() -> list:
        """Get list of supported platforms."""
        return list(Constants.SUPPORTED_PLATFORMS.keys())
    
    @staticmethod
    def is_platform_supported(platform: str) -> bool:
        """Check if a platform is supported."""
        return platform.lower().strip() in Constants.SUPPORTED_PLATFORMS