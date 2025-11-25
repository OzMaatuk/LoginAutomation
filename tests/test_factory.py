import logging
import pytest

from login_automation.login.factory import FactoryLogin
from login_automation.login.linkedin import LoginLinkedIn
from login_automation.login.manual import LoginManually
from login_automation.constants.linkedin import ConstantsLinkedIn


logger = logging.getLogger(__name__)


def test_create_linkedin_login(playwright_page_no_data):
    page = playwright_page_no_data

    obj = FactoryLogin.create_login('linkedin', page)

    assert isinstance(obj, LoginLinkedIn)


def test_create_manual_login(playwright_page_no_data):
    page = playwright_page_no_data

    obj = FactoryLogin.create_login('manual', page)

    assert isinstance(obj, LoginManually)


def test_create_unknown_platform_raises(playwright_page_no_data):
    page = playwright_page_no_data

    with pytest.raises(Exception, match=r"not supported"):
        FactoryLogin.create_login('this_platform_does_not_exist', page)


def test_constants_type_mismatch_logs_warning(caplog, playwright_page_no_data):
    page = playwright_page_no_data
    caplog.set_level(logging.WARNING)

    # pass an arbitrary object which won't match ConstantsLinkedIn
    FactoryLogin.create_login('linkedin', page, constants=object())

    assert any("Constants type mismatch" in r.message for r in caplog.records)
