import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)

driver.quit()
