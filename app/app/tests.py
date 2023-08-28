""" Sample tests"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test calc module"""

    def test_add(self):
        """test add function"""
        res = calc.add(5, 5)

        self.assertEqual(res, 10)

    def test_substract(self):
        """test substract"""
        res = calc.substract(5, 2)

        self.assertEqual(res, 3)

    def test_substract_string_args(self):
        res = calc.substract([2, 4], 2)

        self.assertRaises(TypeError, res)
