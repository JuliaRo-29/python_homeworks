from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo_checkout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    driver.get("https://www.saucedemo.com/")

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Иван", "Петров", "123456")

    checkout_page.click_continue()

    total_price = checkout_page.get_total_price()

    assert total_price == "Total: $58.29", f"Ожидалась сумма 'Total: $58.29', получено '{total_price}'"

    driver.quit()
