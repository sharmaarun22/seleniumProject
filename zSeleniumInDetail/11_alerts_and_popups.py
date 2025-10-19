# alerts_and_popups_demo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

# HTML page with alerts
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>JavaScript Alert & Popup Demo</h2>

    <button onclick="alert('Welcome to Selenium!')">Simple Alert</button><br><br>

    <button onclick="confirm('Do you want to continue?')">Confirmation Alert</button><br><br>

    <button onclick="prompt('Enter your name:')">Prompt Alert</button>
  </body>
</html>
"""

# Open inline HTML
driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

# ====== SIMPLE ALERT ======
print("\n===== ⚠️ Simple Alert =====")
driver.find_element(By.XPATH, "//button[text()='Simple Alert']").click()
time.sleep(1)

alert = Alert(driver)
print("Alert Text:", alert.text)
alert.accept()
print("Simple alert accepted ✅")

# ====== CONFIRMATION ALERT ======
print("\n===== ❓ Confirmation Alert =====")
driver.find_element(By.XPATH, "//button[text()='Confirmation Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.dismiss()  # or alert.accept()
print("Confirmation alert dismissed ❌")

# ====== PROMPT ALERT ======
print("\n===== 💬 Prompt Alert =====")
driver.find_element(By.XPATH, "//button[text()='Prompt Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.send_keys("Arun Sharma")
time.sleep(1)
alert.accept()
print("Prompt alert accepted with input ✅")

# ====== AUTHENTICATION POPUP ======
print("\n===== 🔒 Authentication Popup =====")
# Demo: "https://the-internet.herokuapp.com/basic_auth"
# The site requires username and password (admin:admin)
# URL Format: https://username:password@URL

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)
message = driver.find_element(By.TAG_NAME, "p").text
print("Authentication success message:", message)

driver.quit()
