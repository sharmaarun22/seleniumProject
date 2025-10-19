from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

driver.close()
