from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementsPage


def test_go_to_page_elements(browser):
    de_mo_qa = DemoQa(browser)
    page = ElementsPage(browser)

    de_mo_qa.visit()
    assert de_mo_qa.equal_url()

    de_mo_qa.btn_element.click()
    assert page.equal_url()

    assert de_mo_qa.icon.exist()
    assert de_mo_qa.btn_sidebar_firs.exist()
    assert de_mo_qa.btn_sidebar_firs_textbox.exist()





