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
    result = generate_diff(file_path1, file_path2, 'stylish')
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
    result = generate_diff(file_path3, file_path4, 'stylish')
    assert result == expected_result


def test_generate_diff_big_json(file_path5, file_path6):
    expected_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: \n              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    result = generate_diff(file_path5, file_path6, 'stylish')
    assert result == expected_result


def test_generate_diff_big_yaml(file_path7, file_path8):
    expected_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: \n              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    result = generate_diff(file_path7, file_path8, 'stylish')
    assert result == expected_result


def test_generate_diff_plain(file_path5, file_path6):
    expected_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file_path5, file_path6, 'plain')
    assert result == expected_result


def test_generate_diff_plain_yml(file_path7, file_path8):
    expected_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file_path7, file_path8, 'plain')
    assert result == expected_result


def test_generate_diff_f_json(file_path5, file_path6):
    expected_result = """{"common": {"  + follow": "false", \
"    setting1": "Value 1", "  - setting2": 200, "  - setting3": "true", \
"  + setting3": "null", "  + setting4": "blah blah", "  + setting5": \
{"key5": "value5"}, "setting6": {"doge": {"  - wow": "", "  + wow": \
"so much"}, "    key": "value", "  + ops": "vops"}}, "group1": {"  - baz": \
"bas", "  + baz": "bars", "    foo": "bar", "  - nest": {"key": "value"}, \
"  + nest": "str"}, "  - group2": {"abc": 12345, "deep": {"id": 45}}, \
"  + group3": {"deep": {"id": {"number": 45}}, "fee": 100500}}"""
    result = generate_diff(file_path5, file_path6, 'json')
    assert result == expected_result


def test_generate_diff_f_json_yml(file_path7, file_path8):
    expected_result = """{"common": {"  + follow": "false", \
"    setting1": "Value 1", "  - setting2": 200, "  - setting3": "true", \
"  + setting3": "null", "  + setting4": "blah blah", "  + setting5": \
{"key5": "value5"}, "setting6": {"doge": {"  - wow": "", "  + wow": \
"so much"}, "    key": "value", "  + ops": "vops"}}, "group1": {"  - baz": \
"bas", "  + baz": "bars", "    foo": "bar", "  - nest": {"key": "value"}, \
"  + nest": "str"}, "  - group2": {"abc": 12345, "deep": {"id": 45}}, \
"  + group3": {"deep": {"id": {"number": 45}}, "fee": 100500}}"""
    result = generate_diff(file_path7, file_path8, 'json')
    assert result == expected_result
