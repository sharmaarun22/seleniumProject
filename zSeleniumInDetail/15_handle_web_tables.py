# handle_webtable.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# --------------------------
# Create inline HTML for demo
# --------------------------
html = """
<html>
  <body style="font-family: Arial; padding: 30px;">
    <h2>Employee Data</h2>
    <table border="1" id="employeeTable" cellspacing="0" cellpadding="5">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Department</th>
          <th>Salary</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>101</td>
          <td>Alice</td>
          <td>QA</td>
          <td>65000</td>
        </tr>
        <tr>
          <td>102</td>
          <td>Bob</td>
          <td>Development</td>
          <td>80000</td>
        </tr>
        <tr>
          <td>103</td>
          <td>Charlie</td>
          <td>HR</td>
          <td>60000</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
"""

driver.get("data:text/html;charset=utf-8," + html)
time.sleep(1)

# --------------------------
# 1️⃣ Locate the table
# --------------------------
table = driver.find_element(By.ID, "employeeTable")

# --------------------------
# 2️⃣ Count number of rows & columns
# --------------------------
rows = driver.find_elements(By.XPATH, "//table[@id='employeeTable']/tbody/tr")
cols = driver.find_elements(By.XPATH, "//table[@id='employeeTable']/thead/tr/th")

print(f"Number of Rows: {len(rows)}")
print(f"Number of Columns: {len(cols)}")

# --------------------------
# 3️⃣ Print all table data
# --------------------------
print("\n===== 🧩 Table Data =====")
for i in range(1, len(rows) + 1):
    for j in range(1, len(cols) + 1):
        cell_xpath = f"//table[@id='employeeTable']/tbody/tr[{i}]/td[{j}]"
        cell_value = driver.find_element(By.XPATH, cell_xpath).text
        print(cell_value, end="\t")
    print()  # New line after each row

# --------------------------
# 4️⃣ Access specific cell (Row 2, Column 3)
# --------------------------
specific_cell = driver.find_element(By.XPATH, "//table[@id='employeeTable']/tbody/tr[2]/td[3]").text
print(f"\nValue at Row 2, Column 3: {specific_cell}")

# --------------------------
# 5️⃣ Extract entire column (Names)
# --------------------------
names = driver.find_elements(By.XPATH, "//table[@id='employeeTable']/tbody/tr/td[2]")
print("\nEmployee Names:")
for name in names:
    print("-", name.text)

# --------------------------
# 6️⃣ Example: Find employee with salary > 65000
# --------------------------
print("\nEmployees with salary > 65000:")
for i in range(1, len(rows) + 1):
    name = driver.find_element(By.XPATH, f"//table[@id='employeeTable']/tbody/tr[{i}]/td[2]").text
    salary = int(driver.find_element(By.XPATH, f"//table[@id='employeeTable']/tbody/tr[{i}]/td[4]").text)
    if salary > 65000:
        print(f"{name} → {salary}")

driver.quit()
