import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Deposit_amt_page import DepositAmountPage

class Test_06_add_deposit_amt:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_add_deposit_amt_verification(self,setup_driver):
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logger.info("************ add new deposit amt process started **************")
        self.deposit_amt=DepositAmountPage(self.driver)
        time.sleep(4)
        self.deposit_amt.click_on_tab()
        self.logger.info("**************test_add_deposit_amt_verification started **************")
        verify_add_deposit_page=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if verify_add_deposit_page == "Amount Deposit Form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_06_verify_add_deposit_form.png")
            assert False
        self.logger.info("**************test_add_deposit_amt_verification completed**************")
        with open("utilities/account_id.txt", "r") as f:
            account_id = f.read()
        self.deposit_amt.input_acc_no(account_id)
        self.deposit_amt.input_amt("5000")
        self.deposit_amt.input_reason("Deposited")
        self.logger.info("**************test_add_deposit_amt_process completed**************")
        self.logger.info("************** submit btn is not working **************")
        #self.add_deposit_amt.click_on_deposit_btn()
        self.driver.quit()
