from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://courses.letskodeit.com/"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)
        return driver