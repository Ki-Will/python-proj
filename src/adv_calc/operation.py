"""
Core arithmetic and statistical helper functions for calcutils.
"""

import math


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def average(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def area_rect(a: float, b: float) -> float:
    """Return the area of a rectangle."""
    return a * b


def circumference(r: float) -> float:
    """Return the circumference of a circle."""
    return 2 * r * math.pi
