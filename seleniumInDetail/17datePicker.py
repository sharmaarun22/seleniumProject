import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def date_picker_with_next_button():
    driver.get("https://jqueryui.com/datepicker/")
    frame = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
    driver.switch_to.frame(frame)
    driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

    expected_date = "25"
    expected_month = "June"
    expected_year = "2024"

    while True:
        actual_month = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-month']").text
        actual_year = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-year']").text

        if actual_month == expected_month and actual_year == expected_year:
            break
        else:
            print(actual_month, actual_year)
            driver.find_element(By.XPATH, "//*[contains(text(),'Next')]").click()

    dates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
    for date in dates:
        if date.text == expected_date:
            date.click()


def date_picker_with_dropdown():
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.find_element(By.XPATH,"//input[@id='departon']").click()

    expected_date = "25"
    expected_month = "Jun"
    expected_year = "2024"

    month_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
    month_dropdown_obj = Select(month_dropdown)
    month_dropdown_obj.select_by_visible_text(expected_month)

    year_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
    year_dropdown_obj = Select(year_dropdown)
    year_dropdown_obj.select_by_visible_text(expected_year)

    dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
    for date in dates:
        if date.text == expected_date:
            date.click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        date_picker_with_next_button()
        time.sleep(1)

        date_picker_with_dropdown()
        time.sleep(5)

    finally:
        driver.quit()
