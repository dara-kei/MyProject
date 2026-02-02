import unittest
from unittest.mock import patch
from my_calculator.my_app import calc_func as f



class TestMyCalculator(unittest.TestCase):
    def testSum(self):
        self.assertEqual(f.summary(2,4), 6)
        self.assertEqual(f.summary(-2, 3), 1)
        self.assertEqual(f.summary(-5, -7), -12)

    def testSub(self):
        self.assertEqual(f.subtraction(9, 5), 4)
        self.assertEqual(f.subtraction(-4, 5), -9)
        self.assertEqual(f.subtraction(-3, -1), -2)


    def testMult(self):
        self.assertEqual(f.multiplication(2, 5), 10)
        self.assertEqual(f.multiplication(-2, 8), -16)
        self.assertEqual(f.multiplication(-6, -5), 30)


    def testDiv(self):
        self.assertEqual(f.division(10, 5), 2)
        self.assertEqual(f.division(-410, 5), -82)
        self.assertEqual(f.division(-100, -25), 4)

    def testDivZeroError(self):
        self.assertRaises(ZeroDivisionError,f.division,100,0)


    def testSquare(self):
        self.assertEqual(f.squaring(2, 3), 8)
        self.assertEqual(f.squaring(-2, 3), -8)
        self.assertEqual(f.squaring(-2, -3), -0.125)


    def testInputValidNum(self):
        with patch("builtins.input", return_value = "6"):
            result = f.input_num("Enter: ")
            self.assertEqual(result, 6.0)

    def testInputInvalidFirstNum(self):
        with patch("builtins.input", side_effect = ["six", "6"]):
            result = f.input_num("Enter: ")
            self.assertEqual(result, 6.0)

    def testInputInvalidNums(self):
        with patch("builtins.input", side_effect = ["six","seven", "two", "one", "6"]):
            result = f.input_num("Enter: ")
            self.assertEqual(result, 6.0)

    def testInputValidOperator(self):
        with patch("builtins.input", return_value = "+"):
            self.assertEqual(f.input_operator(), "+")

    def testInputInvalidOperator(self):
        with patch("builtins.input", side_effect = [",", "+"]):
            self.assertEqual(f.input_operator(), "+")

    def testInputInvalidOperators(self):
        with patch("builtins.input", side_effect = [",",".", ")", "%", "+"]):
            self.assertEqual(f.input_operator(), "+")

    def testCalculate(self):
        self.assertEqual(f.calculate(2,2,"+"), 4)
        self.assertEqual(f.calculate(2, 2, "-"), 0)
        self.assertEqual(f.calculate(2, 7, "*"), 14)
        self.assertEqual(f.calculate(2, 2, "/"), 1)
        self.assertEqual(f.calculate(2, 3, "**"), 8)
        self.assertRaises(ValueError, f.calculate,2, 3, "?")


    if __name__ == "__main__":
        unittest.main()







