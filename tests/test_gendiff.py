from gendiff.scripts.gendiff import generate_diff
import pytest
import json


@pytest.fixture
def file1(tmp_path):
    file_path = tmp_path / "file1.json"
    data = {'key1': 'value1', 'key2': 'value2'}
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return file_path


@pytest.fixture
def file2(tmp_path):
    file_path = tmp_path / "file2.json"
    data = {'key2': 'value2', 'key3': 'value3'}
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return file_path


def test_generate_diff(file1, file2):
    expected_diff = '{\n- key1: value1\n  key2: value2\n+ key3: value3\n}'
    assert generate_diff(file1, file2) == expected_diff


def test_generate_diff_empty(tmp_path):
    empty_file1 = tmp_path / "empty1.json"
    empty_file2 = tmp_path / "empty2.json"

    with open(empty_file1, 'w') as f1, open(empty_file2, 'w') as f2:
        json.dump({}, f1)
        json.dump({}, f2)

    expected_empty_diff = '{\n\n}'
    assert generate_diff(empty_file1, empty_file2) == expected_empty_diff
