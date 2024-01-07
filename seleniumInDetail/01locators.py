from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def css_selector_practice():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("tag and id")

    driver.find_element(By.CSS_SELECTOR, "input.inputtext").clear()
    driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("tag and class")

    driver.find_element(By.CSS_SELECTOR, "input[data-testid='royal_email']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[data-testid='royal_email']").send_keys("tag and attribute")

    driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid='royal_email']").clear()
    driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid='royal_email']").send_keys(
        "tag class and attribute")

    driver.close()


def xpath_practice():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, "//input[@name='email' or @id='email']").clear()
    driver.find_element(By.XPATH, "//input[@name='email' and @id='email']").send_keys("or and demo")
    driver.find_element(By.XPATH, "//input[starts-with(@name, 'em')]").clear()
    driver.find_element(By.XPATH, "//input[contains(@name, 'ail')]").send_keys("contains and starts-with() demo")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    driver.close()


def xpath_axes_practice():
    driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

    text = driver.find_element(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr").text
    print("printing text: " + text)

    print("We are skipping parent and child examples as they are already known.")

    descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr/descendant::*")
    print("Total descendants are: " + str(len(descendants)) + " and their values are as follows: ")
    for i in descendants:
        print(i.text)

    ancestors = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::*")
    print("Total ancestors are: " + str(len(ancestors)))

    following_members = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr/following::*")
    print("Total following members are: " + str(len(following_members)))

    following_siblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr/following-sibling::*")
    print("Total following siblings are: " + str(len(following_siblings)))

    preceding_members = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr/preceding::*")
    print("Total preceding members are: " + str(len(preceding_members)))

    preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'BEML')]/ancestor::tr/preceding-sibling::*")
    print("Total preceding siblings are: " + str(len(preceding_siblings)))

    driver.close()


if __name__ == "__main__":
    xpath_axes_practice()
    # xpath_practice()
    # css_selector_practice()
