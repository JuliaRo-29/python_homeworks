from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, "input")
input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

sleep(2)

button_SkyPro = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(button_SkyPro.text.strip())

sleep(5)

driver.quit()
