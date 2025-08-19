from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, value):
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(value)

    def click_button(self, button_text):
        buttons = self.driver.find_elements(By.CLASS_NAME, "btn")
        for button in buttons:
            if button.text == button_text:
                button.click()
                break

    def get_result_text(self):
        return self.driver.find_element(By.ID, "result").text

    def wait_for_result(self, expected_text, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.ID, "result"), expected_text)
        )
