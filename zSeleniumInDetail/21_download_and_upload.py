import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait  # Added for better file check
from selenium.webdriver.support import expected_conditions as EC  # Added for better file check

# === 1️⃣ Setup Chrome Options for Custom Download Directory ===
download_dir = os.getcwd()  # current working directory
TARGET_FILE_NAME = "dummy.pdf"  # Define the expected file name

chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,  # set download path
    "download.prompt_for_download": False,  # disable prompt
    "download.directory_upgrade": True,
    # Force PDF download instead of opening in browser ===
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True  # to avoid security blocks
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# === 2️⃣ Step 1: Download a File (Using Direct Link) ===
# We will use a reliable, direct download link (W3C dummy PDF)
# Navigating to the PDF link directly initiates the download.
# We don't need to click a button.
driver.get("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
print("➡️ Initiated download from W3C...")

# Wait for download to complete. Checking for file existence is more reliable than time.sleep().
downloaded_file_path = os.path.join(download_dir, TARGET_FILE_NAME)

# Custom loop to wait for the file to appear and complete
start_time = time.time()
timeout = 15  # Max time to wait for download
while not os.path.exists(downloaded_file_path):
    if time.time() - start_time > timeout:
        raise Exception(f"File download failed: {TARGET_FILE_NAME} not found after {timeout} seconds.")
    time.sleep(1)

print(f"✅ File downloaded successfully: {downloaded_file_path}")

# === 3️⃣ Step 2: Upload the Same File ===
# Using a demo upload site
driver.get("https://the-internet.herokuapp.com/upload")

# Wait for the upload element to be present
upload_element_locator = (By.ID, "file-upload")
upload_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(upload_element_locator)
)

# Send the absolute file path to the input field
upload_element.send_keys(downloaded_file_path)
print("➡️ File path sent to upload input.")

# Click the upload button
driver.find_element(By.ID, "file-submit").click()

# Wait a bit and confirm upload
uploaded_text_locator = (By.ID, "uploaded-files")
uploaded_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(uploaded_text_locator)
).text

# Verification uses the expected file name (dummy.pdf)
if TARGET_FILE_NAME in uploaded_text:
    print(f"✅ File uploaded successfully. Confirmed file name: {uploaded_text}")
else:
    raise Exception(f"File upload failed. Expected '{TARGET_FILE_NAME}', but uploaded files are: {uploaded_text}")

# === 4️⃣ Cleanup ===
# Clean up the downloaded file
if os.path.exists(downloaded_file_path):
    os.remove(downloaded_file_path)
    print(f"🧹 Cleaned up file: {TARGET_FILE_NAME}")

time.sleep(2)
driver.quit()