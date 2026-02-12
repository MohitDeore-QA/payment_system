import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class MiniStatement :

    mini_statement_page_tab="//a[normalize-space()='Mini Statement']"
    acc_no="//input[@name='accountno']"
    submit_btn="//input[@name='AccSubmit']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_statement_tab(self):
        self.driver.find_element(By.XPATH, self.mini_statement_page_tab).click()

    def enter_account_no(self, account_id):
        self.driver.find_element(By.XPATH, self.acc_no).send_keys(account_id)

    def click_submit_btn(self):
        self.driver.find_element(By.XPATH, self.submit_btn).click()