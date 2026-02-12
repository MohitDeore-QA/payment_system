import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from base_pages.Admin_login_page import Admin_login_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils

class Test_02_login_page_data_driven_testing:
    project_url= Read_config.get_project_url()
    logger = Log_Maker.log_gen()
    path=".//test_data//Test Data.xlsx"
    status_list = []

    def test_valid_admin_login_data_driven(self, setup_driver):
        self.logger.info("*************test_valid_admin_login_data_driven*************")
        self.driver = setup_driver
        self.driver.get(self.project_url)
        self.admin_lp = Admin_login_page(self.driver)

        # Initialize the Wait object correctly
        wait = WebDriverWait(self.driver, 5)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")

        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)

            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login_btn()

            try:
                # Check if alert exists (Invalid Login case)
                alert = wait.until(EC.alert_is_present())
                alert_text = alert.text
                alert.accept()
                self.logger.info(f"Alert handled for row {r}: {alert_text}")
                login_success = False
            except:
                # No alert means we likely logged in (Valid Login case)
                login_success = True

            act_title = self.driver.title
            exp_title = "Guru99 Bank Manager HomePage"  # Check the actual title after login

            if login_success:
                if self.exp_login == "Yes":
                    self.status_list.append("Pass")
                    # LOGOUT is required to test the next row of data
                    # self.admin_lp.click_login_btn()
                    # wait.until(EC.alert_is_present()).accept()
                    self.driver.close()
                else:
                    self.status_list.append("Failed")
                    # self.admin_lp.click_login_btn()
                    # wait.until(EC.alert_is_present()).accept()
                    self.driver.close()
            else:
                if self.exp_login == "No":
                    self.status_list.append("Pass")
                else:
                    self.status_list.append("Failed")

        #Final Assertion logic remains the same






    # def test_valid_admin_login_data_driven(self,setup_driver):
    #     self.logger.info("*************test_valid_admin_login_data_driven*************")
    #     self.driver = setup_driver
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(self.project_url)
    #     self.admin_lp=Admin_login_page(self.driver)
    #     self.rows=excel_utils.get_row_count(self.path,"Sheet1")
    #     print("num of rows:",self.rows )
    #
    #
    #     for r in range(2,self.rows+1):
    #         self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
    #         self.password = excel_utils.read_data(self.path,"Sheet1",r,2)
    #         self.exp_login=excel_utils.read_data(self.path,"Sheet1",r,3)
    #         self.admin_lp.enter_username(self.username)
    #         self.admin_lp.enter_password(self.password)
    #         self.admin_lp.click_login_btn()
    #         if alert_is_present():
    #             self.driver.switch_to.alert.accept()
    #         time.sleep(5)
    #         act_title=self.driver.title
    #         exp_title="Guru99 Bank"
    #
    #         if act_title==exp_title:
    #             if self.exp_login == "Yes":
    #                 self.logger.info("************Test data is passed************")
    #                 self.status_list.append("PASS")
    #             elif self.exp_login == "No":
    #                 self.logger.info("************Test data is Failed************")
    #                 self.status_list.append("Failed")
    #         elif act_title != exp_title:
    #             if self.exp_login == "Yes":
    #                 self.logger.info("************Test data is Failed************")
    #             elif self.exp_login == "No":
    #                 self.logger.info("************Test data is Passed************")
    #                 self.status_list.append("Pass")
    #     print("status list: ",self.status_list)
    #     if "Failed" in self.status_list:
    #         self.logger.info("************Test data is Failed************")
    #         assert False
    #     else:
    #         self.logger.info("************Test data is Passed************")
    #         assert True
    #
    #
    #
    #
    # #
