"""
operations.py
Core arithmetic and statistical helper functions for calcutils.
"""
import numpy as np

def add(a: float, b: float) -> float:
	"""Returns the sum of two numbers."""
	return a + b

def multiply(a: float, b: float) -> float:
	"""Returns the product of two numbers."""
	return a * b
def subract(a:float , b: float) -> float :
	return a - b 

def average(numbers: list) -> float:
	"""Returns the arithmetic mean of a list of numbers."""
	if not numbers:
		return 0.0
	return sum(numbers) / len(numbers)
def area_rect(a: float , b: float) -> float:
	return a*b

def circumf(r: float ) -> float :
	return  2*r*np.pi
