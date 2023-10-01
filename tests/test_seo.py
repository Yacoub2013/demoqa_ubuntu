import time

from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementsPage


def test_navigation(browser):
    page = DemoQa(browser)
    page.visit()
    assert browser.title == 'DEMOQA'
    # browser.set_window_size(2000, 2000)
    time.sleep(5)





