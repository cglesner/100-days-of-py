"""module for calculating dot product or inner product of two vectors."""


def calculate(a, b):
    """Calculate the dot product of two vectors of the same length."""
    if len(b) != len(a):
        return None

    product = 0
    for a_i, b_i in zip(a, b):
        try:
            product += a_i*b_i
        except TypeError:
            return None

    return product

def orthogonal(a):
    """Return an arbitrary vector orthogonal to the input vector."""
    return None