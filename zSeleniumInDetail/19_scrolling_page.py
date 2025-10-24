from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# --- 1️⃣ Normal Scrolling Demo ---
driver.get("https://demoqa.com/")
print("✅ Page loaded successfully")

# Scroll down by pixel
print("➡️ Scrolling down by 500 pixels")
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

# Scroll to bottom
print("➡️ Scrolling to the bottom of the page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Scroll back to top
print("➡️ Scrolling back to the top of the page")
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# Scroll a specific element into view (example: “Book Store Application”)
element = driver.find_element(By.XPATH, "//h5[text()='Book Store Application']")
print("➡️ Scrolling element into view")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(2)


# --- 2️⃣ Infinite Scrolling Demo ---
print("\n🚀 Demonstrating Infinite Scrolling...")
driver.get("https://the-internet.herokuapp.com/infinite_scroll")
time.sleep(2)

last_height = driver.execute_script("return document.body.scrollHeight")
scroll_count = 0

while scroll_count < 5:  # Scroll 5 times, can increase if needed
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
