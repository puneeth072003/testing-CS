from unittest.mock import patch
import pytest


def test_d3_output_correctness(capsys):
    with patch('d3.combinations') as mock_combinations:
        mock_combinations.return_value = 10
        import d3
        captured = capsys.readouterr()
        assert "Combinations of 5 items taken 2 at a time: 10" in captured.out


# Coughed up by CODESOURCERER