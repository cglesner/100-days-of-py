"""Module for calculating the cross product of two vectors."""

def calculate(a, b):
    c_1 = a[1]*b[2] - b[1]*a[2]
    c_2 = a[2]*b[0] - a[0]*b[2]
    c_3 = a[0]*b[1] - a[1]*b[0]
    return (c_1, c_2, c_3)