import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import utilities.custom_logger as cl
from traceback import print_stack

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        print(self.driver.title)
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("No valid type available")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element is found")
        except:
            self.log.info("Element not found")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Click on element " + locator + "locator type: " + locatorType)
        except:
            self.log.info("Element not available to click")

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)

        except:
            self.log.info("Element not available for entering the data")

    def isElementPresent(self, locator, locatorType="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present")
                return True
            else:
                self.log.info("Element not present")
                return False
        except:
            self.log.info("Element not matched")
        return element

    def scrollBar(self, navigation="down"):
        if navigation == "down":
            self.driver.execute_script("window.scrollBy(0,500);")
        else:
            self.driver.execute_script("window.scrollBy(0,-500);")

    def readText(self, locator, locatorType):
        message = self.getElement(locator, locatorType)
        return message

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            self.log.info("Unable to take screenshot")