from pages.admin_login_page import AdminLoginPage
from pages.add_account_page import AddAccountPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestAddNewAccount:

    logger = Log_Maker.log_gen()

    def test_add_new_account(self, login):
        driver = login
        self.logger.info("Login started")

        add_account_page = AddAccountPage(driver)
        add_account_page.open_new_account_tab()

        assert add_account_page.get_header_text() == "Add new account form"

        # Reuse stored customer id
        with open("test_data/customer_id.txt", "r") as f:
            cust_id = f.read()

        add_account_page.add_new_account(
            cust_id=cust_id,
            acc_type="Current",
            deposit="500"
        )

        assert add_account_page.get_header_text() == \
               "Account Generated Successfully!!!"

        account_id = add_account_page.get_account_id()

        with open("utils/account_id.txt", "w") as f:
            f.write(account_id)

        self.logger.info("Account created successfully")
