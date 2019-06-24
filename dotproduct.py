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

    a_1, a_2 = a

    # If any components of a are zero, set the corresponding components of b to 1.
    if a_1 == 0:
        return (1, 0)
    elif a_2 == 0:
        return (0, 1)
    else:
        b_1 = 1
        b_2 = -1*a_1/a_2

    return (b_1, b_2)