from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

html = """
<html>
  <body style="font-family: Arial; padding: 40px;">
    <h2>Standard HTML Date Picker</h2>
    <label for="dateInput">Select a date:</label>
    <input type="date" id="dateInput">
  </body>
</html>
"""

# Load inline HTML
driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

# Locate the date input
date_input = driver.find_element(By.ID, "dateInput")

# Clear and send new date (YYYY-MM-DD format)
date_input.clear()
date_input.send_keys("2025-12-25")

print("✅ Standard date selected successfully: 2025-12-25")

time.sleep(2)
driver.quit()
