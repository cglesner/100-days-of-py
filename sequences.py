"""A module for generating numerical sequences."""
import functools


@functools.lru_cache()
def fibonacci(n):
    """Calculate the n-th term in the fibonacci sequence."""
    return n if n in [0, 1] else fibonacci(n - 1) + fibonacci(n - 2)
