"""A module that implements function (in the mathematical sense) objects.
A function is a object that is 1-to-1 and onto mapping. This means that
for every unique input, there is one and only one output value.
"""
from math import fsum, pow


class Pterm:
    """A class that implements a polynomial term."""
    def __init__(self, argument):
        """Store the coefficient and power for later use."""
        self.p, self.c = argument

    def __call__(self, x):
        """Evaluate the pterm at x."""
        return self.c*pow(x, self.p)

    def __eq__(self, other):
        """Define Pterm equality."""
        return self.p == other.p and self.c == other.c


class Poly:
    """A class that implements a polynomial function."""
    def __init__(self, terms):
        """Construct a polynomial using a list of coefficients."""
        self.term_set = {Pterm(t) for t in terms}

    def __call__(self, x):
        """Evaluate this polynomial at a particular input."""
        return fsum(p(x) for p in self.term_set)
