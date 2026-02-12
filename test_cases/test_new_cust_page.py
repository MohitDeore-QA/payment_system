import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from base_pages.Admin_login_page import Admin_login_page
from base_pages.Create_new_cust_page import Create_New_cust_page
class Test_03_new_cust_page:
    project_url = Read_config.get_project_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_header_verification(self, setup_driver):

        self.driver = setup_driver
        self.driver.get(self.project_url)

        self.logger.info("*************test_valid_admin_login_started*************")
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        self.logger.info("************ Login is completed **************")

        self.logger.info("************ Add new customer process started **************")
        self.logger.info("************ Object is created for class-Create_New_cust_page **************")
        self.add_customer= Create_New_cust_page(self.driver)
        self.add_customer.click_on_new_cust_tab()
        page_header=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if page_header == "Add New Customer":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_header_verification.png")
            self.logger.info("*************header_verification_is_not_matched*************")
            self.driver.quit()
            assert False

        self.add_customer.new_cust_name("AutomationTester")
        self.add_customer.select_gender("male")
        self.add_customer.select_dob("30/09/1999")
        self.add_customer.select_address("2nd floor Quality kiosk Technologies Rupa solitire mahape ghansoli")
        self.add_customer.select_city("Mumbai")
        self.add_customer.select_state("Maharastra")
        self.add_customer.select_zip("411019")
        self.add_customer.select_telephone("0987654234567")
        email=f"SDET{int(time.time())}@qk.com"
        self.add_customer.select_email(email)
        self.add_customer.select_email_pass("automation")
        self.add_customer.click_on_btn()
        self.logger.info("**************add_customer process completed **************")

        time.sleep(8)
        self.logger.info("**************check customer registered successfully **************")
        check_cust_reg_succ=self.driver.find_element(By.XPATH,"//p[@class='heading3']").text
        if check_cust_reg_succ == "Customer Registered Successfully!!!":
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\test_header_verification_check_cust_reg.png")
            assert False
        # assert check_cust_reg_succ == "Customer Registered Successfully!!!"

        self.logger.info("**************capturing cust id **************")
        cust_id=self.driver.find_element(By.XPATH, "//td[normalize-space()='Customer ID']/following-sibling::td").text

        self.logger.info("************** storing cust id in Utilities.custid.txt file started **************")
        with open("utilities/customer_id.txt", "w") as f:
            f.write(cust_id)

        self.logger.info("************** storing cust id in Utilities.custid.txt file completed **************")

        self.driver.quit()











