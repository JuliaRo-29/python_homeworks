from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы со страницей онлайн-калькулятора.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы калькулятора с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку вычислений на калькуляторе.

        Args:
            value (str): Значение задержки в секундах.

        Returns:
            None
        """
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(value)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора с указанным текстом.

        Args:
            button_text (str): Текст кнопки (например, '7', '+', '=').

        Returns:
            None
        """
        buttons = self.driver.find_elements(By.CLASS_NAME, "btn")
        for button in buttons:
            if button.text == button_text:
                button.click()
                break

    def get_result_text(self) -> str:
        """
        Получает текст результата вычисления.

        Returns:
            str: Текст результата (например, '15').
        """
        return self.driver.find_element(By.ID, "result").text

    def wait_for_result(self, expected_text: str, timeout: int = 50) -> None:
        """
        Ожидает появления указанного результата на калькуляторе.

        Args:
            expected_text (str): Ожидаемый текст результата.
            timeout (int, optional): Максимальное время ожидания в секундах. По умолчанию 50.

        Returns:
            None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.ID, "result"), expected_text)
        )
