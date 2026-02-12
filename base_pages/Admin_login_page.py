from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait
class Admin_login_page():
    textbox_username_id="//input[@name='uid']"
    textbox_password="//input[@name='password']"
    login_btn_xpath="//input[@name='btnLogin']"
    logout_btn_xpath="//a[normalize-space()='Log out']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def click_logout_btn(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath).click()
