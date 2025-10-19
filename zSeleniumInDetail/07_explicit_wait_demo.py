# 07_explicit_wait_demo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
)
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

# Load demo HTML that simulates delayed element load
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>Explicit Wait Demo</h2>
    <p>Button will appear after 6 seconds...</p>

    <div id="container"></div>

    <script>
      setTimeout(function(){
          let btn = document.createElement("button");
          btn.innerHTML = "Click Me!";
          btn.id = "delayedButton";
          document.getElementById("container").appendChild(btn);
      }, 6000);
    </script>
  </body>
</html>
"""

driver.get("data:text/html;charset=utf-8," + html)

# Start time
start = time.time()

print("⏳ Waiting for button to appear...")

try:
    # Create WebDriverWait instance
    wait = WebDriverWait(
        driver,
        timeout=10,                 # total wait time (seconds)
        poll_frequency=1,           # check every 1 second
        ignored_exceptions=[
            NoSuchElementException, # ignore if element not yet found
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    # Wait until button is visible
    element = wait.until(
        EC.visibility_of_element_located((By.ID, "delayedButton"))
    )

    print("✅ Button found:", element.text)

except Exception as e:
    print("❌ Exception occurred:", type(e).__name__, "-", e)

finally:
    end = time.time()
    print(f"⏱️ Total wait time: {round(end - start, 2)} seconds")
    driver.quit()
