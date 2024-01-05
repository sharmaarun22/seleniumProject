from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_home_page_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        actual_title = self.driver.title
        expected_title = "Your store. Logi"

        if actual_title == expected_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_home_page_title.png")
            self.driver.close()
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administratio"

        if actual_title == expected_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
