from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateCustomerPage(BasePage):

    # Locators (private)
    _tab_new_customer = (By.XPATH, "//a[normalize-space()='New Customer']")
    _header = (By.XPATH, "//p[@class='heading3']")
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
    _customer_id = (By.XPATH, "//td[normalize-space()='Customer ID']/following-sibling::td")

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_customer_tab(self):
        self.click(self._tab_new_customer)

    def get_header_text(self):
        return self.get_text(self._header)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.click(self._gender_male)
        elif gender.lower() == "female":
            self.click(self._gender_female)
        else:
            raise ValueError("Invalid gender provided")

    def create_customer(self, data):
        self.send_keys(self._customer_name, data["name"])
        self.select_gender(data["gender"])
        self.send_keys(self._dob, data["dob"])
        self.send_keys(self._address, data["address"])
        self.send_keys(self._city, data["city"])
        self.send_keys(self._state, data["state"])
        self.send_keys(self._zip, data["zip"])
        self.send_keys(self._telephone, data["telephone"])
        self.send_keys(self._email, data["email"])
        self.send_keys(self._password, data["password"])
        self.click(self._submit_btn)

    def get_customer_id(self):
        return self.get_text(self._customer_id)
