import time

from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementsPage


def test_navigation(browser):
    page = DemoQa(browser)
    page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(5)
    browser.set_window_size(2000, 2000)
    time.sleep(5)


def test_visible_nav_bar(browser):
    page = ElementsPage(browser)
    page.visit()
    assert not page.nav.visible()
    browser.set_window_size(700, 700)
    assert page.nav.visible()
