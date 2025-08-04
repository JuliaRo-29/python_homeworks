from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
done_message = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p[id='text']"))
    )
image = driver.find_element(By.CSS_SELECTOR, 'img[alt="award"]')
src_value = image.get_attribute("src")
print(src_value)

driver.quit()
