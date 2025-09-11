from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа на сайте saucedemo.com.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы оформления заказа с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа (имя, фамилия, почтовый индекс).

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает на кнопку продолжения оформления заказа.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Текст с итоговой суммой (например, 'Total: $58.29').
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
