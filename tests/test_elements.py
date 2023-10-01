from conftest import browser
from pages.element_page import ElementsPage


def test_go_to_page_elements(browser):
    page = ElementsPage(browser)
    page.visit()

    assert page.btns_first_menu.check_count_elements(count=9)



