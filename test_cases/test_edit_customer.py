from pages.edit_customer_page import EditCustomerPage
from utils.logger import Log_Maker

class TestEditCustomer:
    logger = Log_Maker.log_gen()

    def test_edit_customer(self, login):

        driver = login

        edit_page = EditCustomerPage(driver)
        edit_page.open_edit_customer_tab()

        # Read stored customer ID
        with open("test_data/customer_id.txt", "r") as f:
            cust_id = f.read()

        edit_page.enter_customer_id(cust_id)
        edit_page.submit_customer_id()

        assert edit_page.get_header_text() == "Edit Customer"

        # Update form using component
        edit_page.customer_form.update_address("Updated Address Mumbai")
        edit_page.customer_form.update_city("Pune")
        edit_page.customer_form.submit_form()
