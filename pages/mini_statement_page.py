from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MiniStatementPage(BasePage):

    _mini_statement_tab = (By.XPATH, "//a[normalize-space()='Mini Statement']")
    _header = (By.XPATH, "//p[@class='heading3']")
    _account_no = (By.XPATH, "//input[@name='accountno']")
    _submit_btn = (By.XPATH, "//input[@name='AccSubmit']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.click(self._mini_statement_tab)

    def get_header_text(self):
        return self.get_text(self._header)

    def enter_account_number(self, account_id):
        self.clear_and_type(self._account_no, account_id)

    def submit(self):
        self.click(self._submit_btn)
