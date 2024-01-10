import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.implicitly_wait(5)

try:
    driver.find_element(By.XPATH, "//a[contains(text(), 'Orange')]").click()
    window_ids = driver.window_handles
    for win_id in window_ids:
        driver.switch_to.window(win_id)
        print(driver.title)

finally:
    driver.quit()

# We can close the specific windows by checking the titles of window in if block

# driver.switch_to.window(win_id)
# if driver.title == "OrangeHRM":
#     driver.close()
