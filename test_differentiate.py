"""Test the functionality of the differentiate module."""

import unittest
import func
from differentiate import d_dx

class TestDDX(unittest.TestCase):
    """Test the behavior of the d_dx function."""
    def test_ddx_basic(self):
        """Test the proper behavior of differentiation for a basic case."""
        f_x = func.PolynomialTerm((4, 5))
        df_dx = func.PolynomialTerm((3, 20))
        self.assertEqual(d_dx(f_x), df_dx)

    def test_ddx_const(self):
        """Test that the d_dx function returns a Pterm that is equal to 0*x^0 when
        operating on a Pterm equal to c*x^0."""
        f_const = func.PolynomialTerm((0, 11))
        df_const_dx = func.PolynomialTerm((0, 0))
        self.assertEqual(d_dx(f_const), df_const_dx)


if __name__ == "__main__":
    unittest.main()