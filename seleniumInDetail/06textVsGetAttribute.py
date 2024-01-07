from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")

email_bar = driver.find_element(By.XPATH, "//input[@id='Email']")
email_bar.clear()
email_bar.send_keys("arun@gmail.com")

print("Text Value of the email_bar is: ", email_bar.text)
print("Get Attribute Value of the email_bar is: ", email_bar.get_attribute("value"))
print("Get Attribute Value of the email_bar is: ", email_bar.get_attribute("type"))

driver.quit()