import pytest
from gendiff.build_diff import generate_diff




@pytest.mark.parametrize("path1, path2, style, expected", [
    ('tests/fixtures/file1s.json', 'tests/fixtures/file2s.json', 'stylish', small_files),
    ('tests/fixtures/file1s.yml', 'tests/fixtures/file2s.yml', 'stylish', small_files),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish', big_files),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'stylish', big_files),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain', big_plain),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'plain', big_plain),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json', big_json),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'json', big_json)
])
def test_all(path1, path2, style, expected):
    with open('tests/fixtures/small_files.txt', 'r') as file:
        small_files = file.read()
    with open('tests/fixtures/big_files.txt', 'r') as file:
        big_files = file.read()
    with open('tests/fixtures/big_plain.txt', 'r') as file:
        big_plain = file.read()
    with open('tests/fixtures/big_json.txt', 'r') as file:
        big_json = file.read()
    assert generate_diff(path1, path2, style) == expected
