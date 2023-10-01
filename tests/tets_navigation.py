import time

from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementsPage


def test_navigation(browser):
    page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    page.visit()
    browser.set_window_size(2000, 2000)

    page.btn_element.click()
    # time.sleep(5)
    browser.refresh()
    browser.back()
    browser.forward()
    #elements_page.equale_url()






