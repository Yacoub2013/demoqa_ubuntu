import time

from conftest import browser
from pages.alerts import Alerts


def test_placeholder(browser):
    page = Alerts(browser)
    page.visit()

    assert not page.alert()
    page.btn_alert.click()
    time.sleep(2)
    assert page.alert()
    page.alert().accept()


def test_alert_text(browser):
    page = Alerts(browser)
    page.visit()
    page.btn_alert.click()
    time.sleep(2)
    assert page.alert().text == "You clicked a button"
    page.alert().accept()
    assert not page.alert()


def test_confirm(browser):
    page = Alerts(browser)
    page.visit()
    page.btn_confirm.click()
    # time.sleep(2)
    page.alert().dismiss()
    time.sleep(2)
    assert page.confirmResult.get_text() == "You selected Cancel"


def test_prompt(browser):
    page = Alerts(browser)
    page.visit()
    page.btn_prompt.click()
    page.alert().send_keys('MyName')
    page.alert().accept()
    assert page.promptResult.get_text() == "You entered MyName"
    time.sleep(5)

