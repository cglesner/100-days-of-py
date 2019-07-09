"""A module that implements function (in the mathematical sense) objects.
A function is a object that is 1-to-1 and onto mapping. This means that
for every unique input, there is one and only one output value.
"""
from math import fsum, pow


class PolynomialTerm:
    """A class that implements a polynomial term."""
    def __init__(self, argument):
        """Store the coefficient and power for later use."""
        self.p, self.c = argument

    def __call__(self, x):
        """Evaluate the pterm at x."""
        return self.c*pow(x, self.p)

    def __eq__(self, other):
        """Define Pterm equality."""
        return (self.p, self.c) == (other.p, other.c)

    def __hash__(self):
        """Define how to determine a hash of this object."""
        return hash((self.p, self.c))


class Polynomial:
    """A class that implements a polynomial function."""
    def __init__(self, terms):
        """Construct a polynomial using a list of coefficients."""
        # Populate initial list.
        term_list = [PolynomialTerm(t) for t in terms]
        reduced_term_list = []
        # check for terms with the same power.
        for a in term_list:
            for i, b in enumerate(reduced_term_list):
                if a.p == b.p:
                    # If the same power is present, replace that power term
                    # with a new PolynomialTerm with the sum of the
                    # coefficients.
                    reduced_term_list[i] = PolynomialTerm((b.p, b.c))
                    continue
            # If we didn't encounter duplicates, simple append.
            reduced_term_list.append(a)

        self.term_set = {reduced_term_list}

    def __call__(self, x):
        """Evaluate this polynomial at a particular input."""
        return fsum(p(x) for p in self.term_set)

    def __eq__(self, other):
        """Define equlaity of polynomials."""
        return self.term_set == other.term_set