from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay_45 = driver.find_element(By.CSS_SELECTOR, "input[id='delay']").send_keys(45)

buttons = driver.find_elements(By.CLASS_NAME, "btn")
for button_text in ["7", "+", "8", "="]:
     for button in buttons:
         if button.text == button_text:
            button.click()

result = WebDriverWait(driver, 50).until(
     EC.text_to_be_present_in_element((By.ID, "result"), "15")
)

result_element = driver.find_element(By.ID, "result")
assert result_element.text == "15", f"Ожидался результат '15', получен '{result_element.text}'"

driver.quit()
