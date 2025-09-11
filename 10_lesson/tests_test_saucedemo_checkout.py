import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Процесс оформления заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест процесса оформления заказа на saucedemo.com")
@allure.description("Проверяет процесс оформления заказа на сайте saucedemo.com: добавление товаров в корзину, заполнение формы и проверка итоговой суммы.")
def test_saucedemo_checkout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открыть сайт saucedemo.com"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Войти с логином 'standard_user' и паролем 'secret_sauce'"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавить товары в корзину: Sauce Labs Backpack, Bolt T-Shirt, Onesie"):
            inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
            inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Начать оформление заказа"):
            cart_page.click_checkout()

        with allure.step("Заполнить форму оформления заказа: имя 'Иван', фамилия 'Петров', индекс '123456'"):
            checkout_page.fill_checkout_form("Иван", "Петров", "123456")

        with allure.step("Нажать кнопку продолжения"):
            checkout_page.click_continue()

        with allure.step("Проверить, что итоговая сумма равна 'Total: $58.29'"):
            total_price = checkout_page.get_total_price()
            assert total_price == "Total: $58.29", f"Ожидалась сумма 'Total: $58.29', получено '{total_price}'"

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
