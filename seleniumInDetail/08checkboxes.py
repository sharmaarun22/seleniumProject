import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

# selecting all the checkboxes
for checkbox in checkboxes:
    checkbox.click()
time.sleep(1)

# unselecting all the checkboxes
for checkbox in checkboxes:
    checkbox.click()
time.sleep(1)

# selecting last 2 checkboxes
for i in range(len(checkboxes)-1, len(checkboxes)-3, -1):
    checkboxes[i].click()
time.sleep(1)

# unselecting selected checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(1)

# selecting tuesday and friday
for checkbox in checkboxes:
    if checkbox.get_attribute("id") in ['tuesday', 'friday']:
        checkbox.click()
time.sleep(1)

driver.quit()
