from gendiff.parcer import read_file
from gendiff.formatter import stylish
from gendiff.fromat_plain import plain
from gendiff.format_json import do_json


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_tree(data1, data2)

    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': do_json,
    }

    return formatters[format](diff)


def build_tree(data1, data2):
    diff = {'type': 'root', 'children': {}}
    all_keys = sorted(data1.keys() | data2.keys())
    for key in all_keys:
        if key in data1 and key not in data2:
            diff['children'][key] = {
                'type': 'deleted',
                'key': key,
                'value': data1[key]
            }
        elif key not in data1 and key in data2:
            diff['children'][key] = {
                'type': 'added',
                'key': key,
                'value': data2[key]
            }
        else:
            if data1[key] == data2[key]:
                diff['children'][key] = {
                    'type': 'unchanged',
                    'key': key,
                    'value': data1[key]
                }
            elif (isinstance(data1[key], dict) and
                  isinstance(data2[key], dict)):
                diff['children'][key] = {
                    'type': 'nested',
                    'key': key,
                    'children': build_tree(data1[key], data2[key])
                }
            elif (isinstance(data1[key], dict) or
                  isinstance(data2[key], dict)):
                diff['children'][key] = {
                    'type': 'changed',
                    'key': key,
                    'value1': data1[key] or data2[key],
                    'value2': data2[key] or data1[key]
                }
            else:
                diff['children'][key] = {
                    'type': 'changed',
                    'key': key,
                    'value1': data1[key],
                    'value2': data2[key]
                }

    return diff
