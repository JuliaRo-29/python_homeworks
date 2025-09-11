from selenium.webdriver.common.by import By


class LoginPage:
    """
    Класс для работы со страницей авторизации на сайте saucedemo.com.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы авторизации с драйвером Selenium.

        Args:
            driver: Объект WebDriver для управления браузером.

        Returns:
            None
        """
        self.driver = driver

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле логина.

        Args:
            username (str): Имя пользователя для ввода.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле пароля.

        Args:
            password (str): Пароль для ввода.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает на кнопку входа.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "login-button").click()
