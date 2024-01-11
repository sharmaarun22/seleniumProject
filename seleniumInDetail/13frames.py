import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def handle_multiple_frames():
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.switch_to.frame("coming google")
    text = driver.find_element(By.LINK_TEXT, "Download Link").text
    print(text)

    # this will focus the driver out of the frame. Before going to next frame, we should come back to default content.
    driver.switch_to.default_content()


def handle_inner_frame():
    driver.get("https://demo.automationtesting.in/Frames.html")
    driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

    outer_frame = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
    driver.switch_to.frame(outer_frame)

    inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
    driver.switch_to.frame(inner_frame)

    driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("testing inner frames")
    driver.switch_to.parent_frame()

    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # handle_multiple_frames()
    handle_inner_frame()

    driver.quit()
