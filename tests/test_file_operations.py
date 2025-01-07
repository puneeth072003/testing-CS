import pytest
import os
from file_operations import read_file, write_file

def test_read_file_valid():
    test_filename = 'test_file.txt'
    test_content = 'This is a test content.'
    with open(test_filename, 'w') as f:
        f.write(test_content)
    read_content = read_file(test_filename)
    assert read_content == test_content
    os.remove(test_filename)

def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file('non_existent_file.txt')

def test_write_file_valid():
    test_filename = 'test_write_file.txt'
    test_content = 'Content to be written.'
    write_file(test_filename, test_content)
    with open(test_filename, 'r') as f:
        written_content = f.read()
    assert written_content == test_content
    os.remove(test_filename)

# Coughed up by CODESOURCERER