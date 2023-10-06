import time

import pytest

from conftest import browser
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tap import BrowserTab
from pages.demoqa import DemoQa
from pages.base_page import BasePage


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'

