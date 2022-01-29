import time

from base.selenium_driver import SeleniumDriver


class PaymentPage(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"
    _allcourses_tab = "//a[text()='ALL COURSES']"
    _course_field = "//div[@class='zen-course-title dynamic-text']//h4[contains(text(), 'JavaScript')]"
    _search_field = "course"
    _search_button = "find-course"
    _enroll_button = "//button[text()= 'Enroll in Course']"
    _buy_button = "//div//button//i[1]"
    _message_text = "//div[@class='cc-payment-outer']//span[text()='Your card number is incomplete.']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterUsername(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clickTab(self):
        self.elementClick(self._allcourses_tab, locatorType="xpath")

    def search(self, course):
        self.sendKeys(course, self._search_field, locatorType="name")

    def searchButton(self):
        self.elementClick(self._search_button, locatorType="class")

    def enroll(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def selectcourse(self):
        self.elementClick(self._course_field, locatorType="xpath")

    def clickBuy(self):
        self.scrollBar("down")
        self.elementClick(self._buy_button, locatorType="xpath")
        time.sleep(5)

    def validateMessage(self):
        actual_message_Text = self.readText(self._message_text, locatorType="xpath")
        print("Actual Message is: " + str(actual_message_Text.text))
        expected_message = "Your card number is incomplete."
        if expected_message == str(actual_message_Text.text):
            print("Matched")
        else:
            print("Unmatched")
        self.scrollBar("up")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterUsername(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def chooseCourse(self, search=""):
        self.clickTab()
        self.search(search)
        self.searchButton()
        self.selectcourse()
        self.enroll()
        self.clickBuy()
        self.validateMessage()
        return True
