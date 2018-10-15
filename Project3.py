'''
Write a Python Program to generate a logic for Password Validator.
1. Using Classes and Objects
2. Log all the Events
3. Write Positive and Negative Unit TestCases.
'''
import re
import argparse

class pwdvalidate:

    def __init__(self, pwd):
        self.pwd = pwd

    def check_length(self):
       if len(self.pwd) < int(8):
            return True
       else:
           return False

    def check_capital(self):
        if re.search(r'[A-Z]+',self.pwd):
            return True
        else:
            return False

    def check_digits(self):
        if re.search(r'[0-9]+',self.pwd):
            return True
        else:
            return False

    def check_special_char(self):
        if re.search('[!@#$%&*+]+',self.pwd):
            return True
        else:
            return False

    def check_lower_case(self):
        if re.search(r'[a-z]+',self.pwd):
            return True
        else:
            return False

if __name__ == '__main__':

    parse = argparse.ArgumentParser()
    parse.add_argument("-p","-password",help="Enter the Password")
    args = parse.parse_args()
    actual = args.p

    obj = pwdvalidate(actual)
    print("Check the Length : {}".format(obj.check_length()))
    print("Check the Capital : {}".format(obj.check_capital()))
    print("Check the Digits : {}".format(obj.check_digits()))
    print("Check the Lower case : {}".format(obj.check_lower_case()))
    print("Check the Special Characters : {}".format(obj.check_special_char()))

else:
    print("Main Part of Project3 is not call.")
