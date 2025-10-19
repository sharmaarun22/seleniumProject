from lib2to3.fixer_util import parenthesize

from encodings.punycode import selective_find

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
driver.implicitly_wait(100)


# self
txt_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'MSTC')]/self::a").text
print(txt_msg)