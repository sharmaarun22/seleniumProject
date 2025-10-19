from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


def check_link_status(url):
    """
    Checks the HTTP status code of a given URL.
    Returns the status code (int) or an error message (str).
    """
    try:
        # Use a HEAD request to be faster and not download the full page content
        # Set a timeout for efficiency
        response = requests.head(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as e:
        # Catch various request exceptions (e.g., DNS failure, timeout)
        return f"Error: {e.__class__.__name__}"


def find_and_check_links(driver, url):
    """
    Navigates to a URL, finds all <a> tags, and checks their status.
    """
    print(f"-> Navigating to: {url}")
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # 1. FIND ALL LINK ELEMENTS
    # Find all elements with the tag 'a' which represents a hyperlink
    links = driver.find_elements(By.TAG_NAME, 'a')

    print(f"\n-> Found {len(links)} links on the page. Starting check...")

    broken_links = 0
    valid_links = 0
    total_links_checked = 0

    # 2. EXTRACT AND CHECK THE URL (HREF ATTRIBUTE)
    for link in links:
        href = link.get_attribute('href')

        # Filter out links that are empty or are JavaScript/anchor links
        if href and href.startswith('http'):
            status = check_link_status(href)
            total_links_checked += 1

            # A status code of 400 or higher is generally considered broken/bad
            if isinstance(status, int) and status >= 400:
                print(f"[BROKEN ❌] Status: {status} | URL: {href}")
                broken_links += 1
            elif isinstance(status, int) and status < 400:
                # 200 (OK) and 3xx (Redirection) are typically considered valid
                print(f"[VALID ✅] Status: {status} | URL: {href}")
                valid_links += 1
            else:
                # This handles the 'Error' string returned from check_link_status
                print(f"[ERROR ⚠️] Status: {status} | URL: {href}")
                broken_links += 1  # Treat connection errors as broken

    # 3. REPORT SUMMARY
    print("\n" + "=" * 50)
    print("LINK CHECK SUMMARY")
    print(f"Total Link Elements Found: {len(links)}")
    print(f"Total HTTP/S Links Checked: {total_links_checked}")
    print(f"Valid Links (Status < 400): {valid_links}")
    print(f"Broken/Error Links (Status >= 400 or Connection Error): {broken_links}")
    print("=" * 50)


# --- EXECUTION ---
if __name__ == "__main__":
    # Initialize the WebDriver (Using Chrome as an example)
    # You might need to adjust this for other browsers (Firefox, Edge) or a remote WebDriver.
    driver = webdriver.Chrome()

    # Use a real website URL for testing!
    test_url = "https://www.google.com"  # Replace with a complex page for a better test

    try:
        find_and_check_links(driver, test_url)
    finally:
        driver.quit()