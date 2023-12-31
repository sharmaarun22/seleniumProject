from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger1 = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger1.info("******* STARTING TEST test_home_page_title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        actual_title = self.driver.title
        expected_title = "Your store. Login"

        if actual_title == expected_title:
            self.logger1.info("******* TEST PASSED SUCCESSFULLY *******")
            self.driver.close()
            assert True
        else:
            self.logger1.info("******* TEST FAILED *******")
            self.driver.save_screenshot(".\\Screenshots\\test_home_page_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger1.info("******* STARTING TEST test_login *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"

        if actual_title == expected_title:
            self.logger1.info("******* TEST PASSED SUCCESSFULLY *******")
            self.driver.close()
            assert True
        else:
            self.logger1.info("******* TEST FAILED *******")
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
