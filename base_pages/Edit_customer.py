import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Edit_customer_page:
    edit_cust_tab="//a[normalize-space()='Edit Customer']"
    customer_id = "//input[@name='cusid']"
    click_sbt_btn="//input[@name='AccSubmit']"

    tab_new_cust_btb = "//a[normalize-space()='New Customer']"
    add_new_cust_header = "//p[@class='heading3']"
    cust_name = "//input[@name='name']"
    gender_m = "//input[@value='m']"
    gender_f = "//input[@value='f']"
    dob = "//input[@id='dob']"
    address = "//textarea[@name='addr']"
    city = "//input[@name='city']"
    state = "//input[@name='state']"
    zip = "//input[@name='pinno']"
    telephone = "//input[@name='telephoneno']"
    email = "//input[@name='emailid']"
    email_pass = "//input[@name='password']"
    click_btn = "//input[@name='sub']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_edit_cust_tab(self):
        self.driver.find_element(By.XPATH,self.edit_cust_tab).click()

    def enter_cust_id(self, cust_id):
        self.driver.find_element(By.XPATH,self.customer_id).send_keys(cust_id)

    def click_on_sbt_btn(self):
        self.driver.find_element(By.XPATH,self.click_sbt_btn).click()

    def select_address(self,enter_address):
        self.driver.find_element(By.XPATH,self.address).send_keys(enter_address)

    def select_city(self,enter_city):
        self.driver.find_element(By.XPATH,self.city).send_keys(enter_city)

    def click_on_btn(self):
        self.driver.find_element(By.XPATH,self.click_btn).click()








