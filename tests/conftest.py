import pytest


@pytest.fixture
def file_path1():
    return "files/file1.json"


@pytest.fixture
def file_path2():
    return "files/file2.json"


@pytest.fixture
def file_path3():
    return "files/file1.yml"


@pytest.fixture
def file_path4():
    return "files/file2.yml"
