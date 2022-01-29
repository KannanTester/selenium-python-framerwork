import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"
    _user_icon = "dropdownMenu1"
    _logout_link = "//a[@href='/logout']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterUsername(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clickUserSettings(self):
        self.elementClick(self._user_icon)

    def clickLogoutLink(self):
        self.elementClick(self._logout_link, locatorType="xpath")
