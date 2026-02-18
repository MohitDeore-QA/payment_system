
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        """Waits for element to be clickable before clicking."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Waits for element visibility, clears it, and sends keys."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retrieves text from an element after ensuring visibility."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def handle_alert(self):
        """Waits for alert, captures text, accepts it, and returns the text."""
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def clear_and_type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def select_by_value(self, locator, value):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        Select(element).select_by_value(value)
