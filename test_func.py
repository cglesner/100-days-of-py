"""Test the func module."""

import unittest
import func

class TestPoly(unittest.TestCase):
    """Test the poly(nomial) class."""
    def test_poly_zero(self):
        """Test the construction of a zero-th order polynomial."""
        p_zero = func.Poly([3])
        self.assertEqual(p_zero.evaluate(0), 3)
        self.assertEqual(p_zero.evaluate(1), 3)
        self.assertEqual(p_zero.evaluate(-1), 3)

    def test_poly_one(self):
        """Test the construction of a first order polynomial."""
        p_one = func.Poly([0, 5])
        self.assertEqual(p_one.evaluate(0), 0)
        self.assertEqual(p_one.evaluate(1), 5)
        self.assertEqual(p_one.evaluate(-1), -5)

    def test_poly_five(self):
        """Test the construction of a fifth order polynomial."""
        p_five = func.Poly([1, 1, 1, 1, 1, 1])
        self.assertEqual(p_five.evaluate(0), 1)
        self.assertEqual(p_five.evaluate(1), 6)
        self.assertEqual(p_five.evaluate(-1), 0)