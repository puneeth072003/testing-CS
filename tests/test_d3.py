# tests/test_d3.py
import pytest
import d3

# Test case to check the output of d3
def test_d3_output(capsys):
    # Capture the output of d3
    d3.result
    captured = capsys.readouterr()
    # Check if the expected output is present in the captured output
    assert "Combinations of 5 items taken 2 at a time: 10.0" in captured.out

# Coughed up by CODESOURCERER