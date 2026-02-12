import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Edit_customer import Edit_customer_page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Create_new_cust_page import Create_New_cust_page
class Test_04_edit_cust_page:
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

        self.logger.info("************ edit customer process started **************")
        self.edit_customer = Edit_customer_page(self.driver)
        self.edit_customer.click_on_edit_cust_tab()
        edit_cust_page_header=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if edit_cust_page_header=="Edit Customer Form":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_edit_customer_tab_ver.png")
            assert False

        with open("utilities/customer_id.txt", "r") as f:
            cust_id = f.read()
        print("Reused Customer ID:", cust_id)

        self.edit_customer.enter_cust_id(cust_id)
        self.edit_customer.click_on_sbt_btn()
        self.logger.info("************ edit customer tab successfully opened **************")
        edit_cust_page_header=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if edit_cust_page_header=="Edit Customer":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_edit_customer_page_header_ver.png")
            assert False
        self.logger.info("************ edit customer tab successfully verified **************")

        time.sleep(3)
        self.edit_customer.select_address("2nd floor Quality kiosk Technologies Rupa solitire mahape ghansoli Navi mumbai")
        self.edit_customer.select_city("Navi Mumbai")

        self.logger.info("************ edit customer tab successfully updated with new info **************")
        # self.edit_customer.click_on_btn()
        self.driver.quit()










