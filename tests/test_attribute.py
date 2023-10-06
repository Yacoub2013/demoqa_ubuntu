from conftest import browser
from tests.text_box import TextBox


def test_placeholder(browser):
    page = TextBox(browser)
    page.visit()

    assert page.first_name.get_dom_attribute('placeholder') == 'Full Name'
