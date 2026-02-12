import pytest
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Add_new_acc_no:

    add_new_acc_tab="//a[normalize-space()='New Account']"
    customer_id="//input[@name='cusid']"
    acc_type_drp_down="//select[@name='selaccount']"
    initial_deposit_amt="//input[@name='inideposit']"
    click_on_sbt_btn="//input[@name='button2']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_new_acc_tab(self):
        self.driver.find_element(By.XPATH,self.add_new_acc_tab).click()

    def enter_cust_id(self, cust_id):
        self.driver.find_element(By.XPATH,self.customer_id).send_keys(cust_id)

    def select_account_type(self, account_type):
        dropdown = Select(
            self.driver.find_element(By.XPATH, self.acc_type_drp_down)
        )
        dropdown.select_by_value(account_type)

    def enter_initial_deposit(self, amt):
        self.driver.find_element(By.XPATH,self.initial_deposit_amt).send_keys(amt)

    def click_on_submit_btn(self):
        self.driver.find_element(By.XPATH,self.click_on_sbt_btn).click()

