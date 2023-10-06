import time

from conftest import browser
from pages.browser_tap import BrowserTab


def test_browser_tab(browser):
    page = BrowserTab(browser)
    page.visit()

    assert len(browser.window_handles) == 1
    page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)

