from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DepositAmountPage(BasePage):

    _deposit_tab = (By.XPATH, "//a[normalize-space()='Deposit']")
    _header = (By.XPATH, "//p[@class='heading3']")
    _account_no = (By.NAME, "accountno")
    _amount = (By.NAME, "ammount")
    _description = (By.NAME, "desc")
    _submit_btn = (By.NAME, "AccSubmit")
    _success_message = (By.XPATH, "//p[@class='heading3']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_deposit_tab(self):
        self.click(self._deposit_tab)

    def get_header_text(self):
        return self.get_text(self._header)

    def deposit_amount(self, account_id, amount, reason):
        self.send_keys(self._account_no, account_id)
        self.send_keys(self._amount, amount)
        self.send_keys(self._description, reason)
        self.click(self._submit_btn)

    def get_success_message(self):
        return self.get_text(self._success_message)
