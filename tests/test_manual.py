import pytest

from login_automation.login.manual import LoginManually


class DummyPage:
    def __init__(self):
        self.called = False

    def wait_for_event(self, event_name, timeout=None):
        self.called = True
        # simulate immediate return


def test_manual_login_calls_wait_for_event():
    page = DummyPage()

    lm = LoginManually(page)
    lm.login()

    assert page.called is True


def test_manual_init_requires_page():
    with pytest.raises(Exception, match=r"Page object is required"):
        LoginManually(None)
