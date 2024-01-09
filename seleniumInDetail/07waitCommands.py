import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")

ec = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                     ElementNotVisibleException,
                                                                     ElementNotSelectableException]
                   )

link_to_click = ec.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Orange')]")))
link_to_click.click()

time.sleep(5)

driver.quit()
