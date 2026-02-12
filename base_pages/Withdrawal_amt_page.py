import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class WithdrawalAmtPage:

    withdrawal_amt_tab="//a[normalize-space()='Withdrawal']"
    account_no="//input[@name='accountno']"
    amount="//input[@name='ammount']"
    reason="//input[@name='desc']"
    submit_btn="//input[@name='AccSubmit']"

    def __init__(self, driver):
        self.driver = driver


    def click_on_withdrawalamt_tab(self):
        self.withdrawal_amt_tab = self.driver.find_element(By.XPATH,self.withdrawal_amt_tab).click()

    def enter_acc_no(self,account_id):
        self.account_no = self.driver.find_element(By.XPATH,self.account_no).send_keys(account_id)

    def enter_amount(self,amount):
        self.amount = self.driver.find_element(By.XPATH,self.amount).send_keys(amount)

    def enter_reason(self,reason):
        self.reason = self.driver.find_element(By.XPATH,self.reason).send_keys(reason)

    def click_on_submit_btn(self):
        self.submit_btn=self.driver.find_element(By.XPATH,self.submit_btn).click()


