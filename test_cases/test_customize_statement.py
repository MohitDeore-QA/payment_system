from pages.admin_login_page import AdminLoginPage
from pages.customize_statement_page import CustomizeStatementPage
from utils.config_reader import Read_config
from utils.logger import Log_Maker


class TestCustomizeStatement:

    logger = Log_Maker.log_gen()

    def test_customize_statement(self, login):
        self.logger.info("Login started")

        driver = login

        statement_page = CustomizeStatementPage(driver)
        statement_page.open_statement_tab()

        assert statement_page.get_header_text() == "Customized Statement Form"

        # Read stored account id
        with open("utils/account_id.txt", "r") as f:
            account_id = f.read()

        statement_page.generate_statement(
            account_id=account_id,
            from_date="01/01/2026",
            to_date="10/02/2026",
            min_value="99",
            txn_number="2"
        )

        self.logger.info("Statement generated successfully")
