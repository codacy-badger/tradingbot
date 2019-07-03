from unittest import TestCase

from src.utils import *


class SomeFunctionality(TestCase):
    def test_functionality(self):
        self.assertEqual(69, some_function(69))

    def test_something(self):
        self.assertTrue('This is it, Chief 👌')

    def test_crash(self):
        self.assertRaises(ZeroDivisionError, lambda a, b: a / b, 1, b=0)


class OtherFunctionality(TestCase):
    def test_bad(self):
        self.assertFalse(True)
