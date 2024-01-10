import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(5)

try:
    rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
    columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")

    print(f"Total rows are {len(rows)}")
    print(f"Total columns are {len(columns)}")

    # print the data of table
    for row in range(2, len(rows) + 1):
        for col in range(1, len(columns) + 1):
            el = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[" + str(col) + "]")
            print(el.text, end="     ")
        print()

    # print the books written by Mukesh
    for row in range(2, len(rows) + 1):
        el = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[" + str(2) + "]")
        if el.text == "Mukesh":
            book = driver.find_element(By.XPATH,
                                       "//table[@name='BookTable']//tr[" + str(row) + "]/td[" + str(1) + "]").text
            print(f"Book written by Mukesh is: {book}")
finally:
    driver.quit()
