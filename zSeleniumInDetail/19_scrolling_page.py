from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open demo page for scroll testing
driver.get("https://the-internet.herokuapp.com/infinite_scroll")

print("✅ Page loaded successfully")

# --- 1️⃣ Scroll down by fixed pixel value ---
print("➡️ Scrolling down by 500 pixels")
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

# --- 2️⃣ Scroll till bottom of the page ---
print("➡️ Scrolling till end of page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# --- 3️⃣ Scroll back up to top ---
print("➡️ Scrolling back to top")
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# --- 4️⃣ Scroll a specific element into view ---
driver.get("https://www.selenium.dev/documentation/webdriver/browser/scrolling/")
time.sleep(2)
element = driver.find_element(By.XPATH, "//h2[text()='Scrolling']")
print("➡️ Scrolling an element into view")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(2)

# --- 5️⃣ Infinite Scrolling Example ---
print("\n🚀 Demonstrating Infinite Scrolling...")
driver.get("https://the-internet.herokuapp.com/infinite_scroll")
time.sleep(2)

last_height = driver.execute_script("return document.body.scrollHeight")

scroll_count = 0
while scroll_count < 5:  # scroll 5 times (you can increase this)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("⚠️ No more new content loaded, stopping scroll.")
        break
    last_height = new_height
    scroll_count += 1
    print(f"✅ Scroll iteration {scroll_count} completed")

print("\n🎯 Scrolling demonstration completed successfully!")
driver.quit()
