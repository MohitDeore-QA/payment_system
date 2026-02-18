from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.customer_form_component import CustomerFormComponent


class EditCustomerPage(BasePage):

    _edit_customer_tab = (By.XPATH, "//a[normalize-space()='Edit Customer']")
    _customer_id = (By.NAME, "cusid")
    _submit_btn = (By.NAME, "AccSubmit")
    _header = (By.XPATH, "//p[@class='heading3']")

    def __init__(self, driver):
        super().__init__(driver)
        self.customer_form = CustomerFormComponent(driver)

    def open_edit_customer_tab(self):
        self.click(self._edit_customer_tab)

    def enter_customer_id(self, cust_id):
        self.send_keys(self._customer_id, cust_id)

    def submit_customer_id(self):
        self.click(self._submit_btn)

    def get_header_text(self):
        return self.get_text(self._header)
