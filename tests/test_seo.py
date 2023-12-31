import time

import pytest

from conftest import browser
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tap import BrowserTab
from pages.demoqa import DemoQa
from pages.base_page import BasePage


def test_navigation(browser):
    page = DemoQa(browser)
    page.visit()
    assert browser.title == 'DEMOQA'
    # browser.set_window_size(2000, 2000)
    time.sleep(5)


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    # time.sleep(2)
    assert page.get_title() == 'DEMOQA'

