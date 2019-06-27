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
    """Return an arbitrary vector orthogonal to the input vector.
    :type a: tuple of floats.
    :return b: tuple of floats.
    """
    if len(a) == 1:
        return None

    # Handle the vector generation one way if any elements
    # of the input vector are zero.
    if not all(a):
        return tuple(0 if a_i else 1 for a_i in a)

    # If none of the elements of a are zero, set the first n-1
    # elements of b to 1. Set the n-th element of b as follows:
    return (1,)*len(a[:-1]) + (-1*sum(a[:-1])/a[-1],)
