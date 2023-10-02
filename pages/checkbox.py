from conftest import browser
from pages.base_page import BasePage
from components.components import WebElement


class CheckBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.plus = WebElement(driver, '#tree-node > div > button.rct-option.rct-option-expand-all > svg')
        self.checkbox = WebElement(driver, 'span.rct-text')
