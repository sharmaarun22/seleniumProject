import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag and id
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("1")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("arun")

# tag and class
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("2")

# tag and attribute
driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys("3")

# tag, class and attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("4")

time.sleep(5)