# dropdown_demo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

# Load inline HTML page with dropdowns
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>Dropdown Demo</h2>

    <h3>Single Select Dropdown</h3>
    <select id="country">
      <option value="in">India</option>
      <option value="us">USA</option>
      <option value="uk">UK</option>
      <option value="jp">Japan</option>
    </select>

    <h3>Multi Select Dropdown</h3>
    <select id="skills" multiple>
      <option value="python">Python</option>
      <option value="java">Java</option>
      <option value="js">JavaScript</option>
      <option value="csharp">C#</option>
    </select>
  </body>
</html>
"""

# Open inline HTML
driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

# --- SINGLE SELECT DROPDOWN ---
print("\n===== 🌏 Single Select Dropdown =====")

country_dropdown = Select(driver.find_element(By.ID, "country"))

# Select by visible text
country_dropdown.select_by_visible_text("India")
print("Selected by visible text: India")

# Select by value
country_dropdown.select_by_value("us")
print("Selected by value: USA")

# Select by index (0-based)
country_dropdown.select_by_index(2)
print("Selected by index: UK")

# Get selected option
selected_option = country_dropdown.first_selected_option
print("Currently selected option:", selected_option.text)

# --- MULTI SELECT DROPDOWN ---
print("\n===== ⚙️ Multi-Select Dropdown =====")

skills_dropdown = Select(driver.find_element(By.ID, "skills"))

# Select multiple options
skills_dropdown.select_by_visible_text("Python")
skills_dropdown.select_by_value("java")
skills_dropdown.select_by_index(2)
print("Multiple options selected")

# Get all selected options
selected_skills = [option.text for option in skills_dropdown.all_selected_options]
print("Selected skills:", selected_skills)

# Get all available options
all_options = [option.text for option in skills_dropdown.options]
print("All available options:", all_options)

# Deselect one option
skills_dropdown.deselect_by_visible_text("Python")
print("Deselected 'Python'")

# Deselect all options
skills_dropdown.deselect_all()
print("All options deselected")

time.sleep(2)
driver.quit()
