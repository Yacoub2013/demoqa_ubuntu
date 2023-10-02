from conftest import browser
from pages.element_page import ElementsPage


def test_page_elements(browser):
    page = ElementsPage(browser)
    page.visit()

    assert page.text_elements.get_text() == 'Elements'


