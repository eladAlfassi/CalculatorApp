import unittest
from executor.calculate_executor import *


class TestCalculateExec(unittest.TestCase):
    calculateExecutor=CalculateExecutor()
    def test_operation_method_with_plus(self):
        expected = "9"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4","5","+")
        self.assertEqual(expected,actual)

    def test_operation_method_with_minus(self):
        expected = "-1"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4","5","-")
        self.assertEqual(expected,actual)

    def test_operation_method_with_multiply(self):
        expected = "20"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4","5","*")
        self.assertEqual(expected,actual)

    def test_operation_method_with_multiply_float(self):
        expected = "13.5"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4.5", "3", "*")
        self.assertEqual(expected, actual)

    def test_operation_method_with_divide(self):
        expected = "16"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("32","2","/")
        self.assertEqual(expected,actual)

    def test_operation_method_with_divide__float(self):
        expected = "1.5"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4.5","3","/")
        self.assertEqual(expected,actual)

    def test_operation_method_with_divide_by_zero(self):
        expected = "BAD OPERATION"
        actual = TestCalculateExec.calculateExecutor._CalculateExecutor__operation("4","0","/")
        self.assertEqual(expected,actual)