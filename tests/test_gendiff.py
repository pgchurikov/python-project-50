from gendiff.build_diff import generate_diff


def test_generate_diff_json(file_path1, file_path2):
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result


def test_generate_diff_yaml(file_path3, file_path4):
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file_path3, file_path4)
    assert result == expected_result
