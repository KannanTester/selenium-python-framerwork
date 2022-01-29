import unittest
from tests.payment_tests import PaymentTests
from tests.navigation_payment_tests import NavigationTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(PaymentTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NavigationTests)

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)