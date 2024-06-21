from gendiff.scripts.gendiff import generate_diff
import json
import pytest


@pytest.fixture
def file1():
    data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22"
    }
    file_path = "files/file1.json"
    with open(file_path, "w") as file:
        json.dump(data, file)
    return file_path


@pytest.fixture
def file2():
    data = {
        "host": "hexlet.io",
        "timeout": 20,
        "proxy": "123.234.53.22",
        "verbose": True
    }
    file_path = "files/file2.json"
    with open(file_path, "w") as file:
        json.dump(data, file)
    return file_path


def test_generate_diff(file1, file2):
    expected_output = (
        '{\n'
        '  - timeout: 50\n'
        '  ?         -\n'
        '  + timeout: 20\n'
        '  ?         +\n'
        '  + verbose: true\n'
        '  - proxy: 123.234.53.22\n'
    )
    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_same_file(file1):
    expected_output = (
        '{\n'
        '  host: hexlet.io\n'
        '  timeout: 50\n'
        '  proxy: 123.234.53.22\n'
    )
    assert generate_diff(file1, file1) == expected_output
