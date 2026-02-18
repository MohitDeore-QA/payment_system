from pages.admin_login_page import AdminLoginPage
from pages.deposit_amount_page import DepositAmountPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestDepositAmount:

    logger = Log_Maker.log_gen()

    def test_deposit_amount(self, setup_driver):

        self.logger.info("Login started")

        driver = setup_driver

        deposit_page = DepositAmountPage(driver)
        deposit_page.open_deposit_tab()

        assert deposit_page.get_header_text() == "Amount Deposit Form"

        # Read stored account ID
        with open("utils/account_id.txt", "r") as f:
            account_id = f.read()

        deposit_page.deposit_amount(
            account_id=account_id,
            amount="5000",
            reason="Deposited"
        )

        assert deposit_page.get_success_message() == \
               "Transaction details of Deposit for Account"

        self.logger.info("Deposit successful")
