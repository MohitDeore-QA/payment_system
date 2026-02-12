import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class DepositAmountPage:

    deposit_amt_tab="//a[normalize-space()='Deposit']"
    enter_acc_no="//input[@name='accountno']"
    enter_amt="//input[@name='ammount']"
    reason_of_deposit="//input[@name='desc']"
    click_on_dep_btn="//input[@name='AccSubmit']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_tab(self):
        self.driver.find_element(By.XPATH,self.deposit_amt_tab).click()

    def input_acc_no(self, account_id):
        self.driver.find_element(By.XPATH, self.enter_acc_no).send_keys(account_id)

    def input_amt(self, amt):
        self.driver.find_element(By.XPATH, self.enter_amt).send_keys(amt)

    def input_reason(self, reason):
        self.driver.find_element(By.XPATH, self.reason_of_deposit).send_keys(reason)

    def click_on_deposit_btn(self):
        self.driver.find_element(By.XPATH, self.click_on_dep_btn).click()