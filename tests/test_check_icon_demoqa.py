import time


from pages.demoqa import DemoQa
from conftest import browser


def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    time.sleep(5)
    assert demo_qa_page.icon.exist()
    assert demo_qa_page.get_url()
