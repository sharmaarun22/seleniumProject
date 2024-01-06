import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        return driver
    elif browser == "edge":
        driver = webdriver.Edge()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##### Pytest HTML Report #####

def pytest_configure(config):
    config._metadata = {
        "Tester": "Arun Sharma",
        "Project Name": "Hybrid Framework Practice",
    }


# It is a hook to delete or modify the environment info from in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA.HOME", None)
    metadata.pop("Plugins", None)
