import os
import tempfile

import pytest


def save_string_to_file(s: str, filename: str):
    with open(filename, 'w') as f:
        f.write(s)


@pytest.fixture
def temp_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, 'test_file.txt')
        yield temp_file_path


# Тесты
def test_save_string_to_file(temp_file):
    test_string = "Hello, World!"
    save_string_to_file(test_string, temp_file)

    with open(temp_file, 'r') as f:
        content = f.read()

    assert content == test_string


def test_save_empty_string_to_file(temp_file):
    test_string = ""
    save_string_to_file(test_string, temp_file)

    with open(temp_file, 'r') as f:
        content = f.read()

    assert content == test_string