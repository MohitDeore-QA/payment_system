import pytest
import time
from utils.logger import Log_Maker
from pages.create_customer_page import CreateCustomerPage


class TestNewCustomer:
    logger = Log_Maker.log_gen()

    def test_create_new_customer(self, login):
        self.driver = login
        self.logger.info("Login successful")

        self.logger.info("--- Starting: Add New Customer Test ---")
        customer_page = CreateCustomerPage(self.driver)
        customer_page.open_new_customer_tab()

        assert customer_page.get_header_text() == "Add New Customer"

        email = f"SDET{int(time.time())}@qk.com"

        customer_data = {
            "name": "AutomationTester",
            "gender": "male",
            "dob": "30/09/1999",
            "address": "Mumbai Office",
            "city": "Mumbai",
            "state": "Maharastra",
            "zip": "411019",
            "telephone": "9876542345",
            "email": email,
            "password": "automation"
        }

        customer_page.create_customer(customer_data)

        assert customer_page.get_header_text() == "Customer Registered Successfully!!!"

        cust_id = customer_page.get_customer_id()

        with open("utils/customer_id.txt", "w") as f:
            f.write(cust_id)

        self.logger.info("Customer created successfully")
