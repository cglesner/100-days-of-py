#!/usr/local/bin/python3.7
"""Test the dotproduct module."""

import unittest
import dotproduct


class TestCalculate(unittest.TestCase):
    """Test the calculate function."""

    def test_calculate_null(self):
        """Test that the dot product of two null vectors is zero. Expects Tuples, returns float."""
        a = (0, 0)
        b = (0, 0)
        self.assertEqual(0, dotproduct.calculate(a, b))

    def test_calculate_orthogonal(self):
        """Test that orthogonal vectors result in a zero product."""
        a = (1, 0)
        b = (0, 1)
        self.assertEqual(0, dotproduct.calculate(a, b))

    def test_calculate_parallel(self):
        """Test that parallel vectors result in the sum of squares of the vector's components."""
        a = (2, 3, 5)
        a2 = 2 * 2 + 3 * 3 + 5 * 5
        self.assertEqual(a2, dotproduct.calculate(a, a))

    def test_calculate_antiparallel(self):
        """Test that anti-parallel vectors result in the negative of the sum of the vector's components."""
        a = (2, 3, 5)
        a_neg = (-2, -3, -5)
        a_a_neg = -1 * (2 * 2 + 3 * 3 + 5 * 5)
        self.assertEqual(a_a_neg, dotproduct.calculate(a, a_neg))

    def test_calculate_examples(self):
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

    def test_calculate_commutivity(self):
        """The dot product is commutable. a dot b = b dot a"""
        a = (2, 3, 5, 7)
        b = (1, 1, 2, 3)
        self.assertEqual(dotproduct.calculate(a, b), dotproduct.calculate(b, a))

    def test_calculate_vector_missmatch(self):
        """Test that the method returns None if vectors of different length are passed in."""
        a = (2, 3, 5)
        b = (7, 11, 13, 17)
        self.assertEqual(dotproduct.calculate(a, b), None)

    def test_calculate_invalid_vector(self):
        """Test that the method returns None if vectors contain invalid elements."""
        a = (2, 3, 5)
        b = (7, 11, 'a')
        self.assertEqual(dotproduct.calculate(a, b), None)


class TestOrthogonal(unittest.TestCase):
    """Test the orthogonal function."""

    def test_orthogonal_1D(self):
        """Test that function returns None if 1-D Vector passed in."""
        a = (2,)
        self.assertEqual(dotproduct.orthogonal(a), None)

    def test_orthogonal_2D(self):
        """Test that the function returns an orthogonal vector if a 2-D Vector is passed in."""
        test_vectors = [(1, 1), (1, 0), (3, -5), (9, 9), (-1, -1), (0, 0), (0, 1), (234.5, -0.666)]

        for vector in test_vectors:
            ortho = dotproduct.orthogonal(vector)
            print(f'Vector: {vector}, Ortho: {ortho}')
            self.assertEqual(dotproduct.calculate(vector, ortho), 0)

    def test_orthogonal_3D(self):
        """Test that the function returns an orthogonal vector if a 3-D Vector is passed in."""
        test_vectors = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]

        for vector in test_vectors:
            ortho = dotproduct.orthogonal(vector)
            print(f'Vector: {vector}, Ortho: {ortho}')
            self.assertEqual(dotproduct.calculate(vector, ortho), 0)

    def test_orthogonal_ND(self):
        """Test that the function returns an orthogonal vector for N-Dimentional Vectors."""
        test_vectors = [(1, 3, 5, 0, 2), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (-23.5, 77.9, 237591.01, 999.088888)]

        for vector in test_vectors:
            ortho = dotproduct.orthogonal(vector)
            print(f'Vector: {vector}, Ortho: {ortho}')
            self.assertEqual(dotproduct.calculate(vector, ortho), 0)


if __name__ == "__main__":
    unittest.main()
