from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CommonPage(BasePage):

    _logout_btn = (By.XPATH, "//a[normalize-space()='Log out']")

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click(self._logout_btn)
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text
