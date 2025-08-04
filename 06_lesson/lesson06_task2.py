from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, "input")
input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

button = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)
button_SkyPro = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(button_SkyPro.text.strip())

driver.quit()
