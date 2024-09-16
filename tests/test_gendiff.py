from gendiff.build_diff import generate_diff
from tests.fixtures.results import small_files
from tests.fixtures.results import big_files
from tests.fixtures.results import big_json
from tests.fixtures.results import big_plain


def test_generate_diff_json(file_path1, file_path2):
    expected_result = small_files
    result = generate_diff(file_path1, file_path2, 'stylish')
    assert result == expected_result


def test_generate_diff_yaml(file_path3, file_path4):
    expected_result = small_files
    result = generate_diff(file_path3, file_path4, 'stylish')
    assert result == expected_result


def test_generate_diff_big_json(file_path5, file_path6):
    expected_result = big_files
    result = generate_diff(file_path5, file_path6, 'stylish')
    assert result == expected_result


def test_generate_diff_big_yaml(file_path7, file_path8):
    expected_result = big_files
    result = generate_diff(file_path7, file_path8, 'stylish')
    assert result == expected_result


def test_generate_diff_plain(file_path5, file_path6):
    expected_result = big_plain
    result = generate_diff(file_path5, file_path6, 'plain')
    assert result == expected_result


def test_generate_diff_plain_yml(file_path7, file_path8):
    expected_result = big_plain
    result = generate_diff(file_path7, file_path8, 'plain')
    assert result == expected_result


def test_generate_diff_f_json(file_path5, file_path6):
    expected_result = big_json
    result = generate_diff(file_path5, file_path6, 'json')
    assert result == expected_result


def test_generate_diff_f_json_yml(file_path7, file_path8):
    expected_result = big_json
    result = generate_diff(file_path7, file_path8, 'json')
    assert result == expected_result
