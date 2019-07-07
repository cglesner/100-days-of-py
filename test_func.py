"""Test the func module."""

import unittest
import func


class TestPterm(unittest.TestCase):
    """Test the P(olynomial)term class."""

    def test_pterm_zero(self):
        """Test the construction of a zero-th order polynomial term."""
        pt_zero = func.Pterm((0, 3))
        self.assertEqual(pt_zero(0), 3)
        self.assertEqual(pt_zero(1), 3)
        self.assertEqual(pt_zero(-1), 3)

    def test_pterm_first(self):
        """Test the construction of a first-order polynomial term."""
        pt_first = func.Pterm((1, 7.5))
        self.assertEqual(pt_first(0), 0)
        self.assertEqual(pt_first(1), 7.5)
        self.assertEqual(pt_first(-1), -7.5)

    def test_pterm_equalitytrue(self):
        """Test that pterm equality checking succeeds when it should."""
        p1 = func.Pterm((2, -5))
        p2 = func.Pterm((2, -5))
        self.assertEqual(p1, p2)

    def test_pterm_equalityfalse(self):
        """Test that pterm equality checking fails when it should."""
        p1 = func.Pterm((3, 7))
        p2 = func.Pterm((3, 8))
        p3 = func.Pterm((4, 7))
        p4 = func.Pterm((4, 8))
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p1, p4)


class TestPoly(unittest.TestCase):
    """Test the poly(nomial) class."""

    def test_poly_zero(self):
        """Test the construction of a zero-th order polynomial."""
        p_zero = func.Poly([(0, 3)])
        self.assertEqual(p_zero(0), 3)
        self.assertEqual(p_zero(1), 3)
        self.assertEqual(p_zero(-1), 3)

    def test_poly_one(self):
        """Test the construction of a first order polynomial."""
        p_one = func.Poly([(0, 0), (1, 5)])
        self.assertEqual(p_one(0), 0)
        self.assertEqual(p_one(1), 5)
        self.assertEqual(p_one(-1), -5)

    def test_poly_five(self):
        """Test the construction of a fifth order polynomial."""
        p_five = func.Poly([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
        self.assertEqual(p_five(0), 1)
        self.assertEqual(p_five(1), 6)
        self.assertEqual(p_five(-1), 0)

    def test_poly_equalitytrue(self):
        """Test that equal polynomials evaluate to equal."""
        f_x = func.Poly([(0, 1), (3, 5)])
        g_x = func.Poly([(3, 5), (0, 1)])
        self.assertEqual(f_x, g_x)


if __name__ == "__main__":
    unittest.main()
