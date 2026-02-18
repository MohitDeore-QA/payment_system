from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomizeStatementPage(BasePage):

    _statement_tab = (By.XPATH, "//a[normalize-space()='Customised Statement']")
    _header = (By.XPATH, "//p[@class='heading3']")
    _account_no = (By.NAME, "accountno")
    _from_date = (By.NAME, "fdate")
    _to_date = (By.NAME, "tdate")
    _min_txn_value = (By.NAME, "amountlowerlimit")
    _num_txn = (By.NAME, "numtransaction")
    _submit_btn = (By.NAME, "AccSubmit")

    def __init__(self, driver):
        super().__init__(driver)

    def open_statement_tab(self):
        self.click(self._statement_tab)

    def get_header_text(self):
        return self.get_text(self._header)

    def generate_statement(self, account_id, from_date, to_date, min_value, txn_number):
        self.send_keys(self._account_no, account_id)
        self.send_keys(self._from_date, from_date)
        self.send_keys(self._to_date, to_date)
        self.send_keys(self._min_txn_value, min_value)
        self.send_keys(self._num_txn, txn_number)
        self.click(self._submit_btn)
