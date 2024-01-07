from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source[:100])

driver.quit()