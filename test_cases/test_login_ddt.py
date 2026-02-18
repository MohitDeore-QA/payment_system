import pytest
from pages.admin_login_page import AdminLoginPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestLogin:

    url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup_driver):

        driver = setup_driver
        self.logger.info("Title verification started")

        driver.get(self.url)
        assert driver.title == "Guru99 Bank Home Page"

    def test_valid_admin_login(self, setup_driver):

        driver = setup_driver
        login_page = AdminLoginPage(driver)

        driver.get(self.url)

        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login()

        assert login_page.get_dashboard_text() == "Guru99 Bank"

    def test_invalid_login(self, setup_driver):

        driver = setup_driver
        login_page = AdminLoginPage(driver)

        driver.get(self.url)

        login_page.enter_username(self.invalid_username)
        login_page.enter_password(self.password)
        login_page.click_login()

        alert_text = login_page.get_alert_text()

        assert alert_text == "User or Password is not valid"
