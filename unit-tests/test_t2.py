import pytest
from t2 import combinations

def test_combinations_valid_input():
  assert combinations(5, 2) == 10

def test_combinations_edge_cases():
  assert combinations(0, 0) == 1
  assert combinations(5, 0) == 1

def test_combinations_invalid_input():
    with pytest.raises(TypeError):
        combinations(5.5, 2)

# Coughed up by CODESOURCERER