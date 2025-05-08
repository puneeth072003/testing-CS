import pytest
import f3
from f2 import combinations
from io import StringIO
import sys

def test_f3_output_correctness(capsys):
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Execute the code in f3.py
    f3.result = combinations(5, 2)
    print(f"Combinations of {f3.n} items taken {f3.r} at a time: {f3.result}")

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Assert the captured output matches the expected output
    assert captured_output.getvalue().strip() == "Combinations of 5 items taken 2 at a time: 10.0"


# Coughed up by CODESOURCERER