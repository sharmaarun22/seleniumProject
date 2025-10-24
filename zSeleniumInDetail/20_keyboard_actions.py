import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
act = ActionChains(driver)

driver.find_element(By.XPATH, '//*[@id="inputText1"]').send_keys("Welcome to Bhopal") #type in first input box

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  #copy
act.send_keys(Keys.TAB).perform()                                         #go to next input box
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()  #paste
time.sleep(1)

driver.close()