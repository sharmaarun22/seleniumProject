# checkbox_radio_demo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

# Load sample HTML (embedded inline)
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>Checkbox and Radio Button Demo</h2>

    <h3>Checkboxes</h3>
    <input type="checkbox" id="python" name="lang" value="Python"> Python<br>
    <input type="checkbox" id="java" name="lang" value="Java"> Java<br>
    <input type="checkbox" id="javascript" name="lang" value="JavaScript"> JavaScript<br><br>

    <h3>Radio Buttons</h3>
    <input type="radio" id="male" name="gender" value="Male"> Male<br>
    <input type="radio" id="female" name="gender" value="Female"> Female<br>
    <input type="radio" id="other" name="gender" value="Other"> Other<br><br>
  </body>
</html>
"""

# Open inline HTML
driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

# --- CHECKBOX SECTION ---
print("\n===== 🧩 Checkbox Demo =====")

# Locate elements
python_cb = driver.find_element(By.ID, "python")
java_cb = driver.find_element(By.ID, "java")
js_cb = driver.find_element(By.ID, "javascript")

# Select Python checkbox if not selected
if not python_cb.is_selected():
    python_cb.click()
print("Python selected?", python_cb.is_selected())

# Select Java checkbox
java_cb.click()
print("Java selected?", java_cb.is_selected())

# If JavaScript is already selected, unselect it
if js_cb.is_selected():
    js_cb.click()
else:
    js_cb.click()
print("JavaScript selected?", js_cb.is_selected())

# --- RADIO BUTTON SECTION ---
print("\n===== 🎯 Radio Button Demo =====")

male_rb = driver.find_element(By.ID, "male")
female_rb = driver.find_element(By.ID, "female")
other_rb = driver.find_element(By.ID, "other")

# Select Male
male_rb.click()
print("Male selected?", male_rb.is_selected())
print("Female selected?", female_rb.is_selected())
print("Other selected?", other_rb.is_selected())

# Change to Female
female_rb.click()
print("\nAfter switching to Female:")
print("Male selected?", male_rb.is_selected())
print("Female selected?", female_rb.is_selected())

driver.quit()
