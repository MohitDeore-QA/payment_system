import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Withdrawal_amt_page import WithdrawalAmtPage

class Test_07_withdrawal_amt:
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

        self.logger.info("*************test_withdrawal_amt_process_started**************")
        self.withdrawalamt = WithdrawalAmtPage(self.driver)
        self.withdrawalamt.click_on_withdrawalamt_tab()
        self.logger.info("**************test_withdrawal_amt_page verification**************")
        check_withdrawal_page=self.driver.find_element(By.XPATH,"(//p[@class='heading3'])[1]").text
        if check_withdrawal_page == "Amount Withdrawal Form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_07_verify_withdrawal-amt_form.png")
            assert False
        self.logger.info("**************test_withdrawal_amt_page verification completed**************")
        self.logger.info("**************test_withdrawal_amt_process_started**************")
        with open("utilities/account_id.txt", "r") as f:
            account_id = f.read()
        self.withdrawalamt.enter_acc_no(account_id)
        self.withdrawalamt.enter_amount("500")
        self.withdrawalamt.enter_reason("cashout")
        self.withdrawalamt.click_on_submit_btn()
        time.sleep(4)
        self.logger.info("**************test_withdrawal_amt_process_completed**************")