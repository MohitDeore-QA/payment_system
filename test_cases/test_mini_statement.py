from pages.admin_login_page import AdminLoginPage
from pages.mini_statement_page import MiniStatementPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestMiniStatement:

    logger = Log_Maker.log_gen()

    def test_mini_statement_form(self, login):

        driver = login

        self.logger.info("Login started")

        mini_statement_page = MiniStatementPage(driver)
        mini_statement_page.open()

        assert mini_statement_page.get_header_text() == "Mini Statement Form"

        self.logger.info("Mini Statement page verified")

        with open("utils/account_id.txt", "r") as f:
            account_id = f.read()

        mini_statement_page.enter_account_number(account_id)

        # mini_statement_page.submit()  # Enable when working
