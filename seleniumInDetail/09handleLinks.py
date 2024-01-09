import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")

list_of_links = driver.find_elements(By.XPATH, "//a")
broken_links_count = 0

# finding out the broken links in the page

for link in list_of_links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        print("server error")
    if res.status_code > 400:
        print(f"{link.text} is a broken link")
        broken_links_count += 1
    else:
        print(f"{link.text} is valid")

print(f"Total broken links are {broken_links_count}")

driver.quit()
