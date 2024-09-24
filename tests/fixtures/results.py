small_files = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

big_files = """{
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

big_plain = """Property 'common.follow' was added with value: false
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

big_json = """[{"type": "nested", "key": "common", "value": \
[{"type": "added", "key": "follow", "value": false}, \
{"type": "unchanged", "key": "setting1", "value": "Value 1"}, \
{"type": "deleted", "key": "setting2", "value": 200}, \
{"type": "changed", "key": "setting3", "value1": true, "value2": null}, \
{"type": "added", "key": "setting4", "value": "blah blah"}, \
{"type": "added", "key": "setting5", "value": {"key5": "value5"}}, \
{"type": "nested", "key": "setting6", "value": \
[{"type": "nested", "key": "doge", "value": \
[{"type": "changed", "key": "wow", "value1": "", "value2": "so much"}]}, \
{"type": "unchanged", "key": "key", "value": "value"}, \
{"type": "added", "key": "ops", "value": "vops"}]}]}, \
{"type": "nested", "key": "group1", "value": \
[{"type": "changed", "key": "baz", "value1": "bas", "value2": "bars"}, \
{"type": "unchanged", "key": "foo", "value": "bar"}, \
{"type": "changed", "key": "nest", "value1": {"key": "value"}, \
"value2": "str"}]}, \
{"type": "deleted", "key": "group2", "value": {"abc": 12345, \
"deep": {"id": 45}}}, \
{"type": "added", "key": "group3", "value": {"deep": {"id": \
{"number": 45}}, "fee": 100500}}]"""
