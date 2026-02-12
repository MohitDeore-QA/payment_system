import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from base_pages.Logout_page import LogoutPage

from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page


class Test_10_logout_page:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_logout_page_verification(self,setup_driver):
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logging_out=LogoutPage(self.driver)
        self.logging_out.click_logout_btn()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "You Have Successfully Logged Out!!"
        time.sleep(2)
        # accept alert (click OK)
        alert.accept()

        self.logger.info("************test_valid_admin_login_ended*************")