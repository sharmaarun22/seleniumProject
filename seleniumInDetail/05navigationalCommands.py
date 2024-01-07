import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.back()
driver.forward()
driver.refresh()

driver.quit()