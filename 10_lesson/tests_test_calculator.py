import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@allure.feature("Функциональность калькулятора")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест онлайн-калькулятора")
@allure.description("Проверяет работу онлайн-калькулятора: выполняется сложение 7 + 8 и проверяется результат.")
def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    try:
        with allure.step("Открыть страницу калькулятора"):
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        with allure.step("Установить задержку вычислений на 45 секунд"):
            page.set_delay("45")

        with allure.step("Выполнить вычисление: 7 + 8 ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Ожидать результат '15'"):
            page.wait_for_result("15")

        with allure.step("Проверить, что результат равен '15'"):
            result = page.get_result_text()
            assert result == "15", f"Ожидался результат '15', получен '{result}'"

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
