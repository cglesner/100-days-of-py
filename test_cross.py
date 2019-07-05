"""Test the functionality of the cross module."""

import unittest
import cross

class TestCalc(unittest.TestCase):
    """Test the functionality of the calculate method."""
    def test_parallel_zero(self):
        """Test that cross product of parallel vectors results
        in a null vector."""
        a = (2, 0, 0)
        b = (5, 0, 0)
        null_vec = (0, 0, 0)
        self.assertEqual(cross.calculate(a, b), null_vec)

    def test_perp_max(self):
        """Test that the cross product of orthogonal vectors
        results in a vector whose magnitude is the product of
        the magnitudes of the input vectors."""
        a = (2, 0, 0)
        b = (0, 3, 0)
        c = (0, 0, 5)
        a_cross_b = (0, 0, 6)
        b_cross_c = (15, 0, 0)
        c_cross_a = (0, 10, 0)
        self.assertEqual(cross.calculate(a, b), a_cross_b)
        self.assertEqual(cross.calculate(b, c), b_cross_c)
        self.assertEqual(cross.calculate(c, a), c_cross_a)

    def test_commute_negative(self):
        """Test that a cross b = -1*(b cross a)."""
        a = (2, 3, 5)
        b = (7, 11, 13)
        a_cross_b = cross.calculate(a, b)
        b_cross_a = cross.calculate(b, a)
        neg_b_cross_a = tuple(-1*i for i in b_cross_a)
        self.assertEqual(a_cross_b, neg_b_cross_a)


if __name__ == "__main__":
    unittest.main()