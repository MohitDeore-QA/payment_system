from pages.admin_login_page import AdminLoginPage
from utils.logger import Log_Maker


class Test01LoginPage:

    logger = Log_Maker.log_gen()

    def test_valid_admin_login(self, login):
        self.logger.info("************* test_valid_admin_login_started *************")

        driver = login
        admin_lp = AdminLoginPage(driver)

        assert admin_lp.get_dashboard_text() == "Guru99 Bank"
        self.logger.info("Dashboard text matched successfully")


    def test_invalid_admin_login(self, login, test_data):
        self.logger.info("************* test_invalid_admin_login_started *************")

        driver = login
        driver.get(test_data["url"])
        admin_lp = AdminLoginPage(driver)
        admin_lp.login(test_data["invalid_username"], test_data["password"])

        alert_text = admin_lp.handle_alert()

        assert alert_text == "User or Password is not valid"
        self.logger.info("Alert message validated successfully")
