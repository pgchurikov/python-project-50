import pytest


@pytest.fixture
def file_path1():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file_path2():
    return "tests/fixtures/file2.json"
