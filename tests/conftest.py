# tests/conftest.py

import logging
import configparser
import os
import pytest
from typing import Generator
from playwright.sync_api import sync_playwright, BrowserContext, Page
from dotenv import load_dotenv
from playwright.sync_api._generated import Playwright as SyncPlaywright


logger = logging.getLogger("pytest")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":  # Log only when tests execute
        if report.passed:
            logger.info(f"PASSED: {report.nodeid}")
        elif report.failed:
            logger.error(f"FAILED: {report.nodeid} - {report.longreprtext}")

@pytest.fixture(scope="session")
def config() -> configparser.ConfigParser:
    """Provides a ConfigParser object initialized with config.ini."""
    logger.info("Loading configuration from pytest.ini")
    config = configparser.ConfigParser()
    config.read("pytest.ini")
    return config

@pytest.fixture(scope="session")
def playwright_instance() -> Generator[SyncPlaywright, None, None]:
    """Starts the Playwright instance once per session."""
    logger.info("Starting Playwright instance...")
    instance = sync_playwright().start()
    yield instance
    logger.info("Stopping Playwright instance...")
    instance.stop()
    logger.info("Playwright instance stopped.")

@pytest.fixture(scope="function")
def playwright_browser_no_data(config: configparser.ConfigParser, playwright_instance: SyncPlaywright) -> Generator[BrowserContext, None, None]:
    """
    Launches a non-persistent browser by creating a new context using the shared playwright_instance.
    """
    try:
        logger.info("Launching non-persistent Playwright browser...")
        headless = config.getboolean("general", "headless", fallback=True)
        browser = playwright_instance.chromium.launch(headless=headless)
        context = browser.new_context()
        logger.info("Non-persistent browser context launched successfully.")
        yield context
        logger.info("Closing non-persistent browser context...")
        context.close()
        browser.close()
        logger.info("Non-persistent browser closed.")
    except Exception as e:
        logger.error(f"Failed to launch non-persistent browser: {e}")
        raise

@pytest.fixture(scope="function")
def playwright_page_no_data(playwright_browser_no_data: BrowserContext) -> Generator[Page, None, None]:
    """Fixture to set up and tear down a Playwright page instance for tests."""
    page = playwright_browser_no_data.pages[0] if playwright_browser_no_data.pages else playwright_browser_no_data.new_page()
    logger.info("Navigating to test page...")
    page.goto("about:blank")
    logger.info("Test page loaded successfully.")
    yield page
    # page.close()

@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Loads environment variables from a .env file."""
    logger.info("Loading environment variables from .env file...")
    load_dotenv()
    logger.info("Environment variables loaded.")

@pytest.fixture(scope="session", autouse=True)
def username(config, load_env) -> str:
    username = os.environ.get("USERNAME")
    if not username:
        username = config.get("user_info", "username", fallback="username")
        if not username:
            raise ValueError("USERNAME is not set in environment variables or config.ini.")
    return username

@pytest.fixture(scope="session", autouse=True)
def password(config, load_env) -> str:
    password = os.environ.get("PASSWORD")
    if not password:
        password = config.get("user_info", "password", fallback="password")
        if not password:
            raise ValueError("PASSWORD is not set in environment variables or config.ini.")
    return password