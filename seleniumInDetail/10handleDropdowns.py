import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

dropdown_element = driver.find_element(By.XPATH, "//select[@id='country']")
drop_down_obj = Select(dropdown_element)

drop_down_obj.select_by_visible_text("Australia")
time.sleep(1)

drop_down_obj.select_by_index(3)
time.sleep(1)

drop_down_obj.select_by_value("canada")
time.sleep(1)

list_of_countries = driver.find_elements(By.XPATH, "//select[@id='country']/option")

for country in list_of_countries:
    print(country.text)
    country.click()
    time.sleep(1)

driver.quit()
