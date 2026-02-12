import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Mini_statement_page import MiniStatement

class Test_08_mini_statement:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_withdrawal_amt_verification(self,setup_driver):
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logger.info("*************mini_statement_process_started**************")
        self.print_ministatement=MiniStatement(self.driver)
        self.print_ministatement.click_on_statement_tab()
        self.logger.info("*************mini_statement_page_verification**************")
        check_mini_statement_page=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if check_mini_statement_page=="Mini Statement Form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_08_verify_mini_statement_form.png")
            assert False
        self.logger.info("*************mini_statement_page_verification_completed**************")

        with open("utilities/account_id.txt", "r") as f:
            account_id = f.read()
        self.print_ministatement.enter_account_no(account_id)
        self.logger.info("*************mini_statement_page_submit_btn_not_working**************")
        #self.print_ministatement.click_submit_btn()

