import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running common setup before method")
    yield
    print("Running common teardown after method")

@pytest.fixture(scope="class")
def oneTimeSetup(request, browser):
    print("Running common one time setup before the method")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Running common one time setup teardown after the method")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")