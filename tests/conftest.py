import pytest


@pytest.fixture
def file_path1():
    return "tests/fixtures/file1s.json"


@pytest.fixture
def file_path2():
    return "tests/fixtures/file2s.json"


@pytest.fixture
def file_path3():
    return "tests/fixtures/file1s.yml"


@pytest.fixture
def file_path4():
    return "tests/fixtures/file2s.yml"


@pytest.fixture
def file_path5():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file_path6():
    return "tests/fixtures/file2.json"


@pytest.fixture
def file_path7():
    return "tests/fixtures/file1.yml"


@pytest.fixture
def file_path8():
    return "tests/fixtures/file2.yml"
