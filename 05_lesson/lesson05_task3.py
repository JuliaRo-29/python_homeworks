from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky")

sleep(2)

search_input.clear()

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Pro")

driver.quit()
