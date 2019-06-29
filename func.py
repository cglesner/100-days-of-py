"""A module that implements function (in the mathematical sense) objects.
A function is a object that is 1-to-1 and onto mapping. This means that
for every unique input, there is one and only one output value.
"""
from math import fsum, pow

class Poly:
    """A class that implements a polynomial function."""
    def __init__(self, coefficients):
        """Construct a polynomial using a list of coefficients."""
        self.coef = coefficients

    def evaluate(self, x):
        """Evaluate this polynomial at a particular input."""
        return fsum(c*pow(x, p) for p, c in enumerate(self.coef))
