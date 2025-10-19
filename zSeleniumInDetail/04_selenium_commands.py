# There are total 5 type of selenium commands

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1️⃣ Get Command
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# 2️⃣ Conditional Commands
# Let's locate a visible element and check its state
downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")

print("Is 'Downloads' link displayed?:", downloads_link.is_displayed())
print("Is 'Downloads' link enabled?:", downloads_link.is_enabled())

downloads_link.click()

# 3️⃣ Browser Commands
# Get another page, then use browser actions
driver.get("https://www.python.org/")
print("\nAfter navigation:")
print("Page Title:", driver.title)

driver.minimize_window()
time.sleep(1)
driver.maximize_window()

# 4️⃣ Navigational Commands
driver.back()       # Go back to selenium.dev
time.sleep(2)
driver.forward()    # Go forward to python.org again
time.sleep(2)
driver.refresh()    # Refresh current page
time.sleep(2)

# 5️⃣ Wait Commands

## Implicit Wait (applies globally)
driver.implicitly_wait(10)

## Explicit Wait
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("Selenium WebDriver\n")

# Optional static wait for demo clarity
time.sleep(3)

# Close the browser
driver.close()   # Closes current tab
driver.quit()    # Ends WebDriver session
