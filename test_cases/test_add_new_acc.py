import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Add_acc_no import Add_new_acc_no

class Test_05_add_new_cust_acc:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_edit_cust_page_verification(self,setup_driver):
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logger.info("************ add new customer acc process started **************")
        self.add_new_acc=Add_new_acc_no(self.driver)
        self.add_new_acc.click_on_add_new_acc_tab()
        verify_add_cust_acc_form=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if verify_add_cust_acc_form =="Add new account form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_05_verify_add_cust_acc_form.png")
            assert False
        with open("utilities/customer_id.txt", "r") as f:
            cust_id = f.read()
        print("Reused Customer ID:", cust_id)
        self.add_new_acc.enter_cust_id(cust_id)
        time.sleep(3)
        self.add_new_acc.select_account_type("Current")
        time.sleep(3)
        self.add_new_acc.enter_initial_deposit("500")
        self.add_new_acc.click_on_submit_btn()
        self.logger.info("************ add new customer acc process completed **************")
        self.logger.info("************ acc generated window is pop-up **************")
        check_acc_gen_successfully=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if check_acc_gen_successfully=="Account Generated Successfully!!!":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_05_verify_acc_gen_successfully.png")
            assert False

        time.sleep(3)
        self.logger.info("**************capturing account_id **************")
        account_id=self.driver.find_element(By.XPATH, "//td[normalize-space()='Account ID']/following-sibling::td").text
        time.sleep(2)
        self.logger.info("************** storing account id in Utilities.account_id.txt file started **************")
        with open("utilities/account_id.txt", "w") as f:
            f.write(account_id)
        time.sleep(3)
        self.logger.info("************** storing account id in Utilities.account_id.txt file completed **************")
        self.driver.quit()





