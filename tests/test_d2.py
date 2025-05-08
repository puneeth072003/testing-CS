import pytest
from d2 import combinations
from q1 import factorial


def test_combinations_valid_input():
    assert combinations(5, 2) == 10.0


def test_combinations_edge_cases():
    assert combinations(0, 0) == 1.0
    assert combinations(5, 0) == 1.0


def test_combinations_invalid_input():
    with pytest.raises(TypeError):
        combinations(5, 'a')


# Coughed up by CODESOURCERER