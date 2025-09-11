from selenium.webdriver.common.by import By


class CartPage:
    """
    Класс для работы со страницей корзины на сайте saucedemo.com.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы корзины с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "checkout").click()

    def get_cart_items(self) -> list[str]:
        """
        Получает список названий товаров в корзине.

        Returns:
            list[str]: Список строк с названиями товаров в корзине.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
