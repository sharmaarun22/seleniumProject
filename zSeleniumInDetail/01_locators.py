import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(f"Title of the page is : {driver.title}")
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.NAME, "Email").send_keys("arun.sharma@outlook.com")
driver.find_element(By.ID, "Password").send_keys("P@ssword1")
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links are {len(links)}")
