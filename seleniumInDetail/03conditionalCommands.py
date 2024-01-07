from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

search_bar = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Is search bar enabled: ", search_bar.is_enabled())
print("Is search bar displayed: ", search_bar.is_displayed(), "\n")

male_checkbox = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_checkbox = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default status of checkboxes")
print("Is male selected: ", male_checkbox.is_selected())
print("Is female selected: ", female_checkbox.is_selected(), "\n")

male_checkbox.click()

print("Status of checkboxes after selecting male")
print("Is male selected: ", male_checkbox.is_selected())
print("Is female selected: ", female_checkbox.is_selected(), "\n")

female_checkbox.click()

print("Status of checkboxes after selecting female")
print("Is male selected: ", male_checkbox.is_selected())
print("Is female selected: ", female_checkbox.is_selected())

driver.quit()