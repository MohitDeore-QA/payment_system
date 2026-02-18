# pages/admin_login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminLoginPage(BasePage):
    # Encapsulated Locators (Data)
    username_field = (By.XPATH, "//input[@name='uid']")
    password_field = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//input[@name='btnLogin']")
    logout_button = (By.XPATH, "//a[normalize-space()='Log out']")
    dashboard_header = (By.XPATH, "//h2[normalize-space()='Guru99 Bank']")

    def __init__(self, driver):
        super().__init__(driver)

    # Encapsulated Methods (Actions)
    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)

    def get_dashboard_text(self):
        return self.get_text(self.dashboard_header)

    def logout(self):
        self.click(self.logout_button)