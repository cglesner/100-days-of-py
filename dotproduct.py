"""module for calculating dot product or inner product of two vectors."""

def calculate(a, b):
    """calculate the dot product of two vectors."""

    product = 0
    for a_i, b_i in zip(a, b):
        product += a_i*b_i

    return product