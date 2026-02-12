from selenium import webdriver
from selenium.webdriver.common.by import By

class Create_New_cust_page:
    tab_new_cust_btb="//a[normalize-space()='New Customer']"
    add_new_cust_header="//p[@class='heading3']"
    cust_name="//input[@name='name']"
    gender_m="//input[@value='m']"
    gender_f="//input[@value='f']"
    dob= "//input[@id='dob']"
    address="//textarea[@name='addr']"
    city="//input[@name='city']"
    state="//input[@name='state']"
    zip="//input[@name='pinno']"
    telephone="//input[@name='telephoneno']"
    email="//input[@name='emailid']"
    email_pass="//input[@name='password']"
    click_btn="//input[@name='sub']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_new_cust_tab(self):
        self.driver.find_element(By.XPATH,self.tab_new_cust_btb).click()

    def new_cust_name(self,customer_name):
        self.driver.find_element(By.XPATH,self.cust_name).send_keys(customer_name)

    def select_gender(self,gender):
        if gender=="male":
            self.driver.find_element(By.XPATH,self.gender_m).click()
        elif gender=="female":
            self.driver.find_element(By.XPATH,self.gender_f).click()
        else:
            self.driver.find_element(By.XPATH,self.gender_m).click()

    def select_dob(self,enter_dob):
        self.driver.find_element(By.XPATH,self.dob).send_keys(enter_dob)

    def select_address(self,enter_address):
        self.driver.find_element(By.XPATH,self.address).send_keys(enter_address)

    def select_city(self,enter_city):
        self.driver.find_element(By.XPATH,self.city).send_keys(enter_city)

    def select_state(self,enter_state):
        self.driver.find_element(By.XPATH,self.state).send_keys(enter_state)

    def select_zip(self,enter_zip):
        self.driver.find_element(By.XPATH,self.zip).send_keys(enter_zip)

    def select_telephone(self,enter_telephone):
        self.driver.find_element(By.XPATH,self.telephone).send_keys(enter_telephone)

    def select_email(self,enter_email):
        self.driver.find_element(By.XPATH,self.email).send_keys(enter_email)

    def select_email_pass(self,enter_email_pass):
        self.driver.find_element(By.XPATH,self.email_pass).send_keys(enter_email_pass)

    def click_on_btn(self):
        self.driver.find_element(By.XPATH,self.click_btn).click()




