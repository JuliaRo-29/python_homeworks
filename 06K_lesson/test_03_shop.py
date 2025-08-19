from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Иван")
driver.find_element(By.ID, "last-name").send_keys("Иванов")
driver.find_element(By.ID, "postal-code").send_keys("654321")

driver.find_element(By.ID, "continue").click()

total_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
)
total_text = total_element.text

assert total_text == "Total: $58.29", f"Ожидалась сумма 'Total: $58.29', получено '{total_text}'"

driver.quit()
