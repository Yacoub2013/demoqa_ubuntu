import time

from conftest import browser
from pages.text_box import TextBox


def test_clear(browser):
    page = TextBox(browser)
    page.visit()

    page.first_name.send_keys('dsfdf')
    time.sleep(2)
    page.first_name.clear()
    time.sleep(3)
    assert page.first_name.get_text() == ''
