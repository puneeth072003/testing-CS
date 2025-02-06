import pytest
import t3
from unittest.mock import patch

def test_t3_output(capsys):
    t3.combinations = lambda n, r: 10
    with patch('builtins.print') as mock_print:
        import t3
        mock_print.assert_called_with('Combinations of 5 items taken 2 at a time: 10')

# Coughed up by CODESOURCERER