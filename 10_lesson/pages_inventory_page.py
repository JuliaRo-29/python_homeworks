from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Класс для работы со страницей каталога товаров на сайте saucedemo.com.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы каталога с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по идентификатору кнопки.

        Args:
            item_id (str): ID кнопки добавления товара (например, 'add-to-cart-sauce-labs-backpack').

        Returns:
            None
        """
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину, нажимая на иконку корзины.

        Returns:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
