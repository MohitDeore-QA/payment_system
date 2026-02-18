from pages.admin_login_page import AdminLoginPage
from pages.withdrawal_amount_page import WithdrawalAmountPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestWithdrawalAmount:

    logger = Log_Maker.log_gen()

    def test_withdrawal_amount(self, login):

        driver = login

        self.logger.info("Login started")

        withdrawal_page = WithdrawalAmountPage(driver)
        withdrawal_page.open_withdrawal_tab()

        assert withdrawal_page.get_header_text() == "Amount Withdrawal Form"

        # Read stored account id
        with open("test_data/account_id.txt", "r") as f:
            account_id = f.read()

        withdrawal_page.withdraw_amount(
            account_id=account_id,
            amount="500",
            reason="cashout"
        )

        assert withdrawal_page.get_success_message() == \
               "Transaction details of Withdrawal for Account"

        self.logger.info("Withdrawal successful")
