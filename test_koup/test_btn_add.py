import time

from conftest import browser
from pages.herokuapp import Herokuapp, HerokuappAdd


def test_btn_add(browser):
    page = Herokuapp(browser)
    page_add = HerokuappAdd(browser)
    page.visit()
    assert page.add_remove.get_text() == 'Add/Remove Elements'
    page.add_remove.click()
    #time.sleep(5)
    assert page_add.equal_url()
    assert page_add.add_element.get_text() == 'Add Element'
    assert page_add.add_element.get_dom_attribute('onclick') == 'addElement()'
    for i in range(4):
        page_add.add_element.click()

    # time.sleep(5)
    assert page_add.btn_delete.check_count_elements(4)

    # time.sleep(5)

    while page_add.btn_delete.exist():
        page_add.btn_delete.click()
    #
    # time.sleep(5)
    assert not page_add.btn_delete.exist()
