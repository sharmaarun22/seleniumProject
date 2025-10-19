# browser_windows_demo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

# --- Step 1: Load Main Page ---
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>Main Window</h2>
    <p>This is the main window.</p>
    <button onclick="window.open('https://www.python.org', '_blank');">Open Python.org</button><br><br>
    <button onclick="window.open('https://www.selenium.dev', '_blank');">Open Selenium.dev</button>
  </body>
</html>
"""

driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

main_window = driver.current_window_handle
print("Main window handle:", main_window)

# --- Step 2: Open New Tabs ---
driver.find_element(By.XPATH, "//button[text()='Open Python.org']").click()
driver.find_element(By.XPATH, "//button[text()='Open Selenium.dev']").click()
time.sleep(2)

# --- Step 3: Get All Window Handles ---
all_windows = driver.window_handles
print("\nAll window handles:", all_windows)
print("Total windows open:", len(all_windows))

# --- Step 4: Switch and Print Titles ---
print("\n===== 🔍 Window Titles =====")
for handle in all_windows:
    driver.switch_to.window(handle)
    print(f"Window Handle: {handle}")
    print("Title:", driver.title)
    print("-" * 40)

# --- Step 5: Close a Specific Window by Title ---
target_title = "Welcome to Python.org"
for handle in all_windows:
    driver.switch_to.window(handle)
    if driver.title == target_title:
        print(f"\nClosing window with title: {target_title}")
        driver.close()
        break

# --- Step 6: Switch Back to Main Window ---
driver.switch_to.window(main_window)
print("\nBack to main window:", driver.title)

# --- Step 7: Cleanup ---
time.sleep(2)
driver.quit()
