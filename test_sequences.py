#!/usr/local/bin/python3.7
"""Test the sequences module."""

import unittest
import sequences


class TestFibonacci(unittest.TestCase):
    """Class to test the fibonacci sequence generator."""

    def test_fibonacci_zero(self):
        """Test that the generator yields zero as the zero-th term in the sequence."""
        self.assertEqual(sequences.fibonacci(0), 0)

    def test_fibonacci_one(self):
        """Test that the generator yields 1 as the 1st term in the sequence."""
        self.assertEqual(sequences.fibonacci(1), 1)

    def test_fibonacci_two(self):
        """Test that the generator yields 1 as the 2nd term in the sequence."""
        self.assertEqual(sequences.fibonacci(2), 1)

    def test_fibonacci_twenty(self):
        """Test that the function returns the correct valule for the 20th term in the sequence."""
        self.assertEqual(sequences.fibonacci(20), 6765)

    def test_fibonacci_thirty(self):
        """Test that the function returns the correct valule for the 30th term in the sequence."""
        self.assertEqual(sequences.fibonacci(30), 832040)

    def test_fibonacci_fourty(self):
        """Test that the function returns the correct valule for the 40th term in the sequence."""
        self.assertEqual(sequences.fibonacci(40), 102334155)

    def test_fibonacci_100(self):
        """Test that the function returns the correct valule for the 100th term in the sequence."""
        self.assertEqual(sequences.fibonacci(100), 354224848179261915075)

    def test_fibonacci_300(self):
        """Test that the function returns the correct valule for the 300th term in the sequence."""
        self.assertEqual(sequences.fibonacci(300), 222232244629420445529739893461909967206666939096499764990979600)
