# Difference between find_element and find_elements based on 5 different conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

time.sleep(2)

print("\n===== 1️⃣ Single element given to find_element =====")
try:
    elem = driver.find_element(By.LINK_TEXT, "Downloads")
    print("find_element: Found element ->", elem.text)
except NoSuchElementException:
    print("find_element: Element not found")

print("\n===== 2️⃣ Multiple elements given to find_element =====")
try:
    # There are multiple <a> tags on the page
    elem = driver.find_element(By.TAG_NAME, "a")
    print("find_element: Found first matching element ->", elem.text)
except NoSuchElementException:
    print("find_element: Element not found")

print("\n===== 3️⃣ Single element given to find_elements =====")
elems = driver.find_elements(By.LINK_TEXT, "Downloads")
print("find_elements: Found", len(elems), "elements")
for e in elems:
    print("→", e.text)

print("\n===== 4️⃣ Multiple elements given to find_elements =====")
elems = driver.find_elements(By.TAG_NAME, "a")
print("find_elements: Found", len(elems), "elements (multiple matches)")
print("First 3 examples:", [e.text for e in elems[:3]])

print("\n===== 5️⃣ Element not present (for both) =====")
try:
    driver.find_element(By.ID, "non_existent_id")
    print("find_element: Found element (unexpected)")
except NoSuchElementException:
    print("find_element: ❌ NoSuchElementException raised")

elems = driver.find_elements(By.ID, "non_existent_id")
print("find_elements: Found", len(elems), "elements (should be 0)")

driver.quit()
