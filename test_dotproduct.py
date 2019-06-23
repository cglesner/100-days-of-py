#!/usr/local/bin/python3.7
"""Test the dotproduct module."""

import unittest
import dotproduct


class TestDotProduct(unittest.TestCase):
    """Test the dotproduct module."""

    def test_dotproduct_null(self):
        """Test that the dot product of two null vectors is zero. Expects Tuples, returns float."""
        a = (0, 0)
        b = (0, 0)
        self.assertEqual(0, dotproduct.calculate(a, b))


    def test_dotproduct_orthogonal(self):
        """Test that orthogonal vectors result in a zero product."""
        a = (1, 0)
        b = (0, 1)
        self.assertEqual(0, dotproduct.calculate(a, b))

    def test_dotproduct_parallel(self):
        """Test that parallel vectors result in the sum of squares of the vector's components."""
        a = (2, 3, 5)
        a2 = 2*2 + 3*3 + 5*5
        self.assertEqual(a2, dotproduct.calculate(a, a))

    def test_dotproduct_antiparallel(self):
        """Test that anti-parallel vectors result in the negative of the sum of the vector's components."""
        a = (2, 3, 5)
        a_neg = (-2, -3, -5)
        a_a_neg = -1*(2*2 + 3*3 + 5*5)
        self.assertEqual(a_a_neg, dotproduct.calculate(a, a_neg))

    def test_dotproduct_examples(self):
        """Test arbitrary examples of dot products."""
        a = (2, 3, 5)

        b = (1, 0, 0)
        a_b = 2
        self.assertEqual(a_b, dotproduct.calculate(a, b))

        c = (0, 1, 0)
        a_c = 3
        self.assertEqual(a_c, dotproduct.calculate(a, c))

        d = (0, 0, 1)
        a_d = 5
        self.assertEqual(a_d, dotproduct.calculate(a, d))

        e = (5, 2, 3)
        a_e = 31
        self.assertEqual(a_e, dotproduct.calculate(a, e))

    def test_dotproduct_comutivity(self):
        """The dot product is commutable. a dot b = b dot a"""
        a = (2, 3, 5, 7)
        b = (1, 1, 2, 3)
        self.assertEqual(dotproduct.calculate(a, b), dotproduct.calculate(b, a))

if __name__ == "__main__":
    unittest.main()
