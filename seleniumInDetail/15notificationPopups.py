import time

from selenium import webdriver

"""
Sometimes your browser will throw some notification popups. 
These popups can neither be handled by alert nor we can by pass them them.
The only way to handle these is by disabling the browser notifications.
We can do this using ChromeOptions and passing the object while initializing driver.
"""

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://whatmylocation.com/")

time.sleep(5)

driver.quit()

