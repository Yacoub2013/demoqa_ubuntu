import time

from conftest import browser
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testorevich')
    form_page.user_email.send_keys('test@test.ru')
    form_page.gender_radio_1.click()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click()
    form_page.current_address.send_keys('vbcvbv cvb cvb c cvb cvb')
    time.sleep(5)
    form_page.btn_submit.click_force()
    time.sleep(5)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    time.sleep(5)

