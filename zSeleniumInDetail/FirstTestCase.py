#Test Case
#--
# 1) Open Web Browser (Chrome/firefox/Edge).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
#3) Enter username (Admin).
# 4) Enter password (admin123).
#5) Click on Login.
# 6) Capture title of the home page. (Actual title)
#7) Verify title of the page: OrangeHRM (Expected)
#8) close browser


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# serv_obj = Service('C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
# driver = webdriver.Chrome(service=serv_obj)

# If we put the chrome driver at "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts" or "C:\Users\aruns\AppData\Local\Programs\Python\Python313\Scripts"
# then no need to pass the driver path in constructor. Hence above lines can be written as

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//button[@type="submit"]').click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

driver.close()