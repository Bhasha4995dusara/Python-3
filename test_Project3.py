from Project3 import pwdvalidate
import unittest
import logging

class test_Project3(unittest.TestCase):

    logging.basicConfig(filename='./test_project3.log', level=logging.DEBUG,format='%(asctime)s %(message)s', )

    def setUp(self):
        self.test_cases = pwdvalidate("User@12")
        logging.info("Information Logging")

    def tearDown(self):
        return True

    def test_check_length(self):
        logging.debug("Debug logging for length check")
        self.assertTrue(self.test_cases.check_length())
        #self.assertFalse(self.test_cases.check_length())

    def test_is_capital(self):
        logging.debug("Debug logging for check capital")
        self.assertTrue(self.test_cases.check_capital())
        #self.assertFalse(self.test_cases.check_capital())

    def test_is_digits(self):
        logging.debug("Debug logging for check digit")
        self.assertTrue(self.test_cases.check_digits())
        #self.assertFalse(self.test_cases.check_digits())

    def test_is_lower(self):
        logging.debug("Debug logging for check lower")
        self.assertTrue(self.test_cases.check_lower_case())
        #self.assertFalse(self.test_cases.check_lower_case())

    def test_is_special_char(self):
        logging.debug("Debug logging for check special character")
        self.assertTrue(self.test_cases.check_special_char())
        #self.assertFalse(self.test_cases.check_special_char())


if __name__ == '__main__':
    unittest.main()