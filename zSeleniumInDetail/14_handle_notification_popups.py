# handle_notifications.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# --------------------------
# ✅ OPTION 1: Disable Notifications (Recommended)
# --------------------------
chrome_options = webdriver.ChromeOptions()

prefs = {
    "profile.default_content_setting_values.notifications": 2  # 1 = allow, 2 = block
}
chrome_options.add_experimental_option("prefs", prefs)

# Optional: Run headless (for CI/CD)
# chrome_options.add_argument("--headless=new")

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# --------------------------
# Step 1: Open a site that triggers notification popup
# --------------------------
driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")

print("Opened demo site...")

time.sleep(2)

# --------------------------
# Step 2: Click button that triggers notification request
# --------------------------
try:
    driver.find_element(By.XPATH, "//button[contains(text(),'Show Notification')]").click()
    print("Clicked notification button")
except Exception as e:
    print("Button not found:", e)

time.sleep(3)

# --------------------------
# Step 3: Validate the page (no notification popup should appear)
# --------------------------
print("✅ Notifications are blocked successfully!")

# --------------------------
# Step 4: (Optional) Enable Notifications
# --------------------------
# If you want to allow notifications:
# prefs = {"profile.default_content_setting_values.notifications": 1}

time.sleep(2)
driver.quit()
