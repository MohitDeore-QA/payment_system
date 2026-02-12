import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class CustomizeStatementPage:

    customize_page_tab="//a[normalize-space()='Customised Statement']"
    acc_no="//input[@name='accountno']"
    from_date="//input[@name='fdate']"
    to_date="//input[@name='tdate']"
    min_txn_value="//input[@name='amountlowerlimit']"
    no_txn="//input[@name='numtransaction']"
    submit_btn="//input[@name='AccSubmit']"

    def __init__(self, driver):
        self.driver = driver

    def click_cust_statement_tab(self):
        self.driver.find_element(By.XPATH,self.customize_page_tab).click()

    def enter_acc_no(self, account_id):
        self.driver.find_element(By.XPATH,self.acc_no).send_keys(account_id)

    def enter_from_date(self, from_date):
        self.driver.find_element(By.XPATH,self.from_date).send_keys(from_date)

    def enter_to_date(self, to_date):
        self.driver.find_element(By.XPATH,self.to_date).send_keys(to_date)

    def enter_txn_value(self, min_value):
        self.driver.find_element(By.XPATH,self.min_txn_value).send_keys(min_value)

    def enter_txn_no(self, txn_number):
        self.driver.find_element(By.XPATH,self.no_txn).send_keys(txn_number)

    def click_on_button(self):
        self.driver.find_element(By.XPATH,self.submit_btn).click()