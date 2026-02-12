import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Customize_statement_page import CustomizeStatementPage

class Test_09_customize_page:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_customize_page_verification(self,setup_driver):
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logger.info("*************customize_page_verification_started**************")
        self.customizepage = CustomizeStatementPage(self.driver)
        self.customizepage.click_cust_statement_tab()
        check_cust_page_tab=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if check_cust_page_tab=="Customized Statement Form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_09_verify_cust_statement_form.png")
            assert False
        self.logger.info("*************customize_page_verification_completed**************")
        with open("utilities/account_id.txt", "r") as f:
            account_id = f.read()
        self.customizepage.enter_acc_no(account_id)
        self.customizepage.enter_from_date("1/01/2026")
        self.customizepage.enter_to_date("10/02/2026")
        self.customizepage.enter_txn_value("99")
        self.customizepage.enter_txn_no("2")
        self.logger.info("**************customize_page_submit_btn_not_working**************")
        #self.customizepage.click_on_button()
        self.logger.info("*************customize_page_process_completed**************")