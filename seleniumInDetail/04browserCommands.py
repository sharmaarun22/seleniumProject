import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[contains(text(), 'Orange')]").click()

time.sleep(5)

# driver.close()
driver.quit()