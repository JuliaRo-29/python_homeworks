from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    page.wait_for_result("15")

    result = page.get_result_text()
    assert result == "15", f"Ожидался результат '15', получен '{result}'"

    driver.quit()
