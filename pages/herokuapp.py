from conftest import browser
from pages.base_page import BasePage
from components.components import WebElement


class Herokuapp(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.add_remove = WebElement(driver, '#content > ul > li:nth-child(2) > a')
        self.add_element = WebElement(driver, '#content > div > button')
        self.btn_delete = WebElement(driver, '#elements > button:nth-child(1)')


class HerokuappAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.add_element = WebElement(driver, '#content > div > button')
        self.btn_delete = WebElement(driver, '#elements > button')
        self.row = WebElement(driver, 'div.row>div:nth-child(1)')
