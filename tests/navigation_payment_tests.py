import time
import unittest
import pytest
from page.payment_page import PaymentPage
from page.login_page import LoginPage
from utilities.teststatus import TestStatus

@pytest.mark.userfixtures("oneTimeSetup", "setUp")
class NavigationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.nav = LoginPage(self.driver)
        self.pay = PaymentPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.nav.clickLoginLink()
        self.nav.enterUsername("samaya2021@gmail.cm")
        self.nav.enterPassword("python")
        self.nav.clickLoginButton()

    @pytest.mark.run(order=2)
    def test_payment_failed(self):
        result = self.pay.chooseCourse("javascript")
        # result = self.pay.buy("samaya2021@gmail.cm", "python", "javascript")
        self.ts.mark(result, "Success")
        self.nav.clickUserSettings()
        self.nav.clickLogoutLink()