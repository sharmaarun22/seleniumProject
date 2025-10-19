from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup ---
driver = webdriver.Chrome()
driver.maximize_window()
# Initialize WebDriverWait for synchronization
wait = WebDriverWait(driver, 10)

# The URL for the jQuery UI Datepicker demo
DEMO_URL = "https://jqueryui.com/datepicker/"
DATE_TO_SELECT = "25"  # The date we want to pick

print(f"-> Navigating to Demo URL: {DEMO_URL}")
driver.get(DEMO_URL)

# 1. Handle the Iframe (Crucial Step for this Demo Site!)
# The date picker input is INSIDE an iframe on the demo page.
# If you don't switch to the iframe, you'll get a NoSuchElementException.
try:
    # Wait for the iframe to be present and switch to it
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))
    print("-> Switched successfully to the iframe.")

    # 2. Click the Input Field to Open the Date Picker
    date_field_locator = (By.ID, "datepicker")
    # Wait for the input field to be clickable
    date_input = wait.until(EC.element_to_be_clickable(date_field_locator))

    print("-> Clicking the date input field.")
    date_input.click()

    # 3. Wait for the Date Picker Calendar to Appear
    # We can wait for a unique element of the calendar, like the date '25' itself.
    # The XPath targets a <td> element with the text '25' that has a link inside it.
    date_25_locator = (By.XPATH, f"//td/a[text()='{DATE_TO_SELECT}']")

    print(f"-> Waiting for date '{DATE_TO_SELECT}' to become visible and clicking...")

    # Wait until the date element is visible and clickable
    date_element = wait.until(EC.element_to_be_clickable(date_25_locator))
    date_element.click()

    print(f"-> Date {DATE_TO_SELECT} clicked.")

    # 4. Verification
    # Get the selected value from the input field
    selected_date = date_input.get_attribute("value")

    print(f"\n✅ Date selected successfully: {selected_date}")

    # NOTE: The format on this page is typically MMDDYYYY, so it should contain '25'
    if DATE_TO_SELECT in selected_date:
        print("Test PASS: The selected date matches the expected input.")
    else:
        print("Test FAIL: The selected date is not as expected.")

except Exception as e:
    print(f"\n❌ Test Failed. An error occurred during the date selection process.")
    print(f"Error Type: {e.__class__.__name__}")
    print(f"Error Message: {e}")

finally:
    # Clean up by switching back to the default content and quitting the driver
    driver.switch_to.default_content()
    time.sleep(2)
    driver.quit()