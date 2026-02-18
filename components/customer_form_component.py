from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomerFormComponent(BasePage):

    _customer_name = (By.NAME, "name")
    _gender_male = (By.XPATH, "//input[@value='m']")
    _gender_female = (By.XPATH, "//input[@value='f']")
    _dob = (By.ID, "dob")
    _address = (By.NAME, "addr")
    _city = (By.NAME, "city")
    _state = (By.NAME, "state")
    _zip = (By.NAME, "pinno")
    _telephone = (By.NAME, "telephoneno")
    _email = (By.NAME, "emailid")
    _password = (By.NAME, "password")
    _submit_btn = (By.NAME, "sub")

    def __init__(self, driver):
        super().__init__(driver)

    def update_address(self, address):
        self.clear_and_type(self._address, address)

    def update_city(self, city):
        self.clear_and_type(self._city, city)

    def submit_form(self):
        self.click(self._submit_btn)
