from conftest import browser
from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_slider = WebElement(driver, '#state ')
        self.state = WebElement(driver, '#state > div > div.css-1hwfws3 > div ')
        self.state_2 = WebElement(driver, '#react-select-3-option-2')
        self.city = WebElement(driver, '#city > div > div.css-1hwfws3 > div ')
        self.city_1 = WebElement(driver, '#react-select-4-option-1')
        self.submit_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
