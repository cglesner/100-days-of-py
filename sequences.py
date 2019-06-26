"""A module for generating numerical sequences."""
import functools


@functools.lru_cache()
def fibonacci(n):
    if n > 1:
        return (fibonacci(n-1) + fibonacci(n-2))
    elif n == 1:
        return 1
    else:
        return 0