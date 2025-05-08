import pytest
import sys
from io import StringIO
from g3 import combinations


def test_g3_output_correctness(capsys):
    # Redirect stdout to capture the print output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Execute the code that prints to stdout
    import g3

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Assert the captured output
    assert "Combinations of 5 items taken 2 at a time: 10" in captured_output.getvalue()


# Coughed up by CODESOURCERER