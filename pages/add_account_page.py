from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddAccountPage(BasePage):

    _add_account_tab = (By.XPATH, "//a[normalize-space()='New Account']")
    _header = (By.XPATH, "//p[@class='heading3']")
    _customer_id = (By.NAME, "cusid")
    _account_type = (By.NAME, "selaccount")
    _initial_deposit = (By.NAME, "inideposit")
    _submit_btn = (By.NAME, "button2")
    _account_id = (By.XPATH, "//td[normalize-space()='Account ID']/following-sibling::td")

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_account_tab(self):
        self.click(self._add_account_tab)

    def get_header_text(self):
        return self.get_text(self._header)

    def add_new_account(self, cust_id, acc_type, deposit):
        self.send_keys(self._customer_id, cust_id)
        self.select_by_value(self._account_type, acc_type)
        self.send_keys(self._initial_deposit, deposit)
        self.click(self._submit_btn)

    def get_account_id(self):
        return self.get_text(self._account_id)
