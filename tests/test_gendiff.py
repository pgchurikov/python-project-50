import pytest
from gendiff.build_diff import generate_diff


@pytest.mark.parametrize("path1, path2, style, expected", [
    (
        'tests/fixtures/file1s.json',
        'tests/fixtures/file2s.json',
        'stylish',
        'tests/fixtures/small_files.txt'
    ),
    (
        'tests/fixtures/file1s.yml',
        'tests/fixtures/file2s.yml',
        'stylish',
        'tests/fixtures/small_files.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'stylish',
        'tests/fixtures/big_files.txt'
    ),
    (
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        'stylish',
        'tests/fixtures/big_files.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'plain',
        'tests/fixtures/big_plain.txt'
    ),
    (
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        'plain',
        'tests/fixtures/big_plain.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'json',
        'tests/fixtures/big_json.txt'
    ),
    (
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        'json',
        'tests/fixtures/big_json.txt'
    )
])
def test_all(path1, path2, style, expected):
    with open(expected, 'r') as file:
        expected = file.read()
    assert generate_diff(path1, path2, style) == expected
