import pytest
import os
from main import main
from unittest.mock import patch

@patch('main.process_content', return_value='processed_content')
def test_main_integration(mock_process_content):
    input_file = 'input.txt'
    output_file = 'output.txt'
    input_content = 'original content'
    with open(input_file, 'w') as f:
        f.write(input_content)
    main()
    with open(output_file, 'r') as f:
        output_content = f.read()
    assert output_content == 'processed_content'
    os.remove(input_file)
    os.remove(output_file)

# Coughed up by CODESOURCERER