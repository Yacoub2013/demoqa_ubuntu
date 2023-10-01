import time
from conftest import browser
from pages.element_page import ElementsPage


def test_visible_btn_sidebar(browser):
    page = ElementsPage(browser)
    page.visit()
    browser.set_window_size(2000, 2000)

    time.sleep(5)

    assert not page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    page = ElementsPage(browser)
    page.visit()
    page.btn_sidebar_first_checkbox.visible()
    page.btn_sidebar_first.click()
    time.sleep(2)
    assert page.btn_sidebar_first_checkbox.not_visible()







