import time

from conftest import browser
from pages.checkbox import CheckBox
from pages.element_page import ElementsPage


def test_go_to_page_elements(browser):
    page = ElementsPage(browser)
    page.visit()

    assert page.btns_first_menu.check_count_elements(count=9)


def test_count_checkbox(browser):
    page = CheckBox(browser)
    page.visit()

    assert page.checkbox.check_count_elements(1)
    page.plus.click()
    #time.sleep(5)
    assert page.checkbox.check_count_elements(17)
    browser.refresh()
    assert page.checkbox.check_count_elements(1)
