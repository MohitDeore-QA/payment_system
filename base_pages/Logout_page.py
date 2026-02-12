from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:
    logout_btn_tab = "//a[normalize-space()='Log out']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_logout_btn(self):
        logout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.logout_btn_tab))
        )
        # Scroll to avoid ElementClickInterceptedException
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", logout_btn
        )

        logout_btn.click()
