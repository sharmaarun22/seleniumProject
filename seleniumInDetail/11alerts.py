import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_data_test = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")

alert_data_test.click()
my_alert = driver.switch_to.alert
print(my_alert.text)
my_alert.send_keys("handling alerts")
my_alert.accept()

time.sleep(5)

alert_data_test.click()
my_alert = driver.switch_to.alert
my_alert.dismiss()

time.sleep(2)

driver.quit()
