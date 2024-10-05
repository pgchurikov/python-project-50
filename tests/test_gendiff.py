import pytest
from gendiff.build_diff import generate_diff


file_path1 = 'tests/fixtures/file1s.json'
file_path2 = 'tests/fixtures/file2s.json'
file_path3 = 'tests/fixtures/file1s.yml'
file_path4 = 'tests/fixtures/file2s.yml'
file_path5 = 'tests/fixtures/file1.json'
file_path6 = 'tests/fixtures/file2.json'
file_path7 = 'tests/fixtures/file1.yml'
file_path8 = 'tests/fixtures/file2.yml'

with open('tests/fixtures/small_files.txt', 'r') as file:
    small_files = file.read()
with open('tests/fixtures/big_files.txt', 'r') as file:
    big_files = file.read()
with open('tests/fixtures/big_plain.txt', 'r') as file:
    big_plain = file.read()
with open('tests/fixtures/big_json.txt', 'r') as file:
    big_json = file.read()


@pytest.mark.parametrize("path1, path2, style, expected", [
    (file_path1, file_path2, 'stylish', small_files),
    (file_path3, file_path4, 'stylish', small_files),
    (file_path5, file_path6, 'stylish', big_files),
    (file_path7, file_path8, 'stylish', big_files),
    (file_path5, file_path6, 'plain', big_plain),
    (file_path7, file_path8, 'plain', big_plain),
    (file_path5, file_path6, 'json', big_json),
    (file_path7, file_path8, 'json', big_json)
])
def test_all(path1, path2, style, expected):
    assert generate_diff(path1, path2, style) == expected
