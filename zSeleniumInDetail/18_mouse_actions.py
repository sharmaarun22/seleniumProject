from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup ---
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)  # Reliable wait mechanism

# Create ActionChains instance
actions = ActionChains(driver)

# --- 1️⃣ Hover Action (and Double Click) ---
HOVER_URL = "https://www.selenium.dev/selenium/web/mouse_interaction.html"
print(f"\n===== 1️⃣ Testing Hover and Double Click on: {HOVER_URL} =====")
driver.get(HOVER_URL)

try:
    # Wait for the elements to be present
    hover_elem = wait.until(EC.presence_of_element_located((By.ID, "hover")))
    double_click_elem = driver.find_element(By.ID, "double-click")

    # 1. Hover action
    actions.move_to_element(hover_elem).perform()
    print("✅ Hovered over element (changes color)")
    time.sleep(1)

    # 2. Double-click
    actions.double_click(double_click_elem).perform()
    # Wait for the text change to confirm the action
    wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "Double-clicked!"))
    print("✅ Double clicked element (Message confirmed)")

except Exception as e:
    print(f"❌ Hover/DoubleClick Test Failed: {e.__class__.__name__}")
finally:
    time.sleep(1)

# --- 2️⃣ Drag and Drop ---
DRAG_DROP_URL = "https://jqueryui.com/droppable/"
print(f"\n===== 2️⃣ Testing Drag and Drop on: {DRAG_DROP_URL} =====")
driver.get(DRAG_DROP_URL)

try:
    # Drag and Drop is usually inside an Iframe on this site
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))
    print("-> Switched to Drag and Drop iframe.")

    source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    target = driver.find_element(By.ID, "droppable")

    # 3. Drag and drop
    actions.drag_and_drop(source, target).perform()

    # Verification: Wait for the target text to change
    wait.until(EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!"))
    print("✅ Drag and Drop completed (Target text confirmed)")

except Exception as e:
    print(f"❌ Drag and Drop Test Failed: {e.__class__.__name__}")
finally:
    driver.switch_to.default_content()  # Switch back to main content
    time.sleep(1)

# --- 3️⃣ Slider Movement (Drag and Drop by Offset) ---
SLIDER_URL = "https://jqueryui.com/slider/"
print(f"\n===== 3️⃣ Testing Slider Movement on: {SLIDER_URL} =====")
driver.get(SLIDER_URL)

try:
    # Slider is also inside an Iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))
    print("-> Switched to Slider iframe.")

    # Locate the slider handle
    slider_handle = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-slider-handle")))

    # Get initial position for verification
    initial_x = slider_handle.location['x']

    # 4. Slider movement (Drag and drop by offset)
    # Move the slider 200 pixels to the right
    x_offset = 200
    actions.drag_and_drop_by_offset(slider_handle, x_offset, 0).perform()
    print(f"-> Attempting to move slider by {x_offset} pixels.")

    # Verification: Check if the slider's x-coordinate has changed
    new_x = slider_handle.location['x']

    if new_x > initial_x:
        print("✅ Slider moved successfully (Position changed confirmed)")
    else:
        print("⚠️ Slider movement failed (Position did not change)")

except Exception as e:
    print(f"❌ Slider Test Failed: {e.__class__.__name__}")
finally:
    driver.switch_to.default_content()
    time.sleep(2)
    driver.quit()