from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

login_input = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
login_input.send_keys("tomsmith")

sleep(2)

password_input = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
password_input.send_keys("SuperSecretPassword!")

sleep(2)

click_loginbutton = driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in")
click_loginbutton.click()

sleep(2)

#success_text = driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
#print (success_text.text.strip())


flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text.strip())

sleep(2)

driver.quit()
