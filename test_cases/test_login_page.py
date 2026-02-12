
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base_pages.Admin_login_page import Admin_login_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker

class Test_01_login_page:
    project_url= Read_config.get_project_url()
    username=Read_config.get_username()
    password=Read_config.get_password()
    invalid_username=Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self,setup_driver):
        self.logger.info("*************Test_01_login_page.*************")
        self.logger.info("*************Test_01_login_page.title_verification*************")
        self.driver = setup_driver
        self.driver.get(self.project_url)
        act_title=self.driver.title
        exp_title="Guru99 Bank Home Page"
        if act_title==exp_title:
            self.logger.info("*************title_verification_is_matched*************")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("*************title_verification_is_not_matched*************")
            self.driver.quit()
            assert False

        # assert act_title == exp_title
        # self.driver.quit()

    def test_valid_admin_login(self,setup_driver):
        self.logger.info("*************test_valid_admin_login_started*************")
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.admin_lp=Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//h2[normalize-space()='Guru99 Bank']").text
        if act_dashboard_text == "Guru99 Bank":
            self.logger.info("*************Dashboard_trext_is_matched*************")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.quit()
            assert False
        # assert act_dashboard_text =="Guru99 Bank"
        # self.driver.quit()

    def test_invalid_invalid_login(self,setup_driver):
        self.logger.info("*************test_invalid_invalid_login_started*************")

        self.driver = setup_driver
        self.driver.get(self.project_url)
        # Enter invalid credentials
        self.admin_lp = Admin_login_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_btn()
        # Validate alert text
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        #self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")

        if alert_text == "User or Password is not valid":
            self.logger.info("*************test_invalid_invalid_login_alert_is_matched*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.driver.close()
            assert False

        self.logger.info("*************providing cust information started ************")

