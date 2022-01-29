import time
import unittest
import pytest
from page.payment_page import PaymentPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.userfixtures("oneTimeSetup", "setUp")
@ddt
class PaymentTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.pay = PaymentPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    #@data(("samaya2021@gmail.cm", "python", "javascript"), ("samaya2021@gmail.cm", "python", "python"), ("samaya2021@gmail.cm", "python", "rest"))
    @data(*getCSVData("C:\\Users\\Samayapoorani Kannan\\PycharmProjects\\practiceProject\\testdata.csv"))
    @unpack
    def test_payment_failed(self, email, pwd, course):
        self.pay.login(email=email, password=pwd)
        result = self.pay.chooseCourse(search=course)
        # result = self.pay.buy("samaya2021@gmail.cm", "python", "javascript")
        self.ts.mark(result, "Success")