# tests/test_d2.py
import pytest
from d2 import combinations

# Test case for valid combinations input
def test_combinations_valid_input():
    # Test combinations with valid n and r
    assert combinations(5, 2) == 10.0

# Test case for edge case where n and r are same
def test_combinations_same_n_r():
    # Test combinations when n and r are equal
    assert combinations(4, 4) == 1.0

# Test case for edge case where r is zero
def test_combinations_zero_r():
    # Test combinations when r is 0
    assert combinations(5, 0) == 1.0

# Test case for combinations with a larger number
def test_combinations_larger_input():
    # Test with slightly larger inputs
    assert combinations(10, 3) == 120.0


# Coughed up by CODESOURCERER