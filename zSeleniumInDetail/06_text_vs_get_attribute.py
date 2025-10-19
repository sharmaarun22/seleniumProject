# text is already a part of dom and cannot be changed while value is usually what user enters in input

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Load a simple HTML content using data URL
html_content = """
<html>
  <body style="font-family: Arial; padding: 20px;">
    <h2>Login Form</h2>

    <label for="username">Username:</label><br>
    <input type="text" id="username" value="Arun Sharma"><br><br>

    <label for="password">Password:</label><br>
    <input type="password" id="password" value="Secret123"><br><br>

    <button id="login">Login</button>
  </body>
</html>
"""

# Open the local HTML content
driver.get("data:text/html;charset=utf-8," + html_content)

time.sleep(1)

# Locate elements
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login")

print("\n===== Username Field =====")
print("text ->", username_input.text)
print("get_attribute('value') ->", username_input.get_attribute("value"))

print("\n===== Password Field =====")
print("text ->", password_input.text)
print("get_attribute('value') ->", password_input.get_attribute("value"))

print("\n===== Login Button =====")
print("text ->", login_button.text)
print("get_attribute('value') ->", login_button.get_attribute("value"))

driver.quit()
