from pages.admin_login_page import AdminLoginPage
from pages.common_page import CommonPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestLogout:

    logger = Log_Maker.log_gen()

    def test_logout(self, login):

        driver = login
        self.logger.info("Login started")

        common_page = CommonPage(driver)
        alert_text = common_page.logout()

        assert alert_text == "You Have Successfully Logged Out!!"

        self.logger.info("Logout successful")
