from gendiff.parcer import read_file
from gendiff.formatters.constant import FORMATTERS


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_tree(data1, data2)

    if format not in FORMATTERS:
        raise ValueError(f'Wrong formatter name: {format}')

    return FORMATTERS[format](diff)


def build_tree(data1, data2):
    diff = {'type': 'root', 'children': []}
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        match (key in data1, key in data2, value1, value2):
            case (True, False, _, _):
                if isinstance(value1, dict):
                    diff['children'].append({
                        'type': 'deleted',
                        'key': key,
                        'children': build_tree(value1, {})['children']
                    })
                else:
                    diff['children'].append({
                        'type': 'deleted',
                        'key': key,
                        'value': value1
                    })
            case (False, True, _, _):
                if isinstance(value2, dict):
                    diff['children'].append({
                        'type': 'added',
                        'key': key,
                        'children': build_tree({}, value2)['children']
                    })
                else:
                    diff['children'].append({
                        'type': 'added',
                        'key': key,
                        'value': value2
                    })
            case (True, True, value1, value2) if value1 == value2:
                if isinstance(value1, dict):
                    diff['children'].append({
                        'type': 'unchanged',
                        'key': key,
                        'children': build_tree(value1, value2)['children']
                    })
                else:
                    diff['children'].append({
                        'type': 'unchanged',
                        'key': key,
                        'value': value1
                    })
            case (True, True, dict(), dict()):
                diff['children'].append({
                    'type': 'nested',
                    'key': key,
                    'children': build_tree(value1, value2)['children']
                })
            case (True, True, _, _):
                if isinstance(value1, dict):
                    diff['children'].append({
                        'type': 'changed',
                        'key': key,
                        'children': build_tree(value1, {})['children'],
                        'value2': value2
                    })
                elif isinstance(value2, dict):
                    diff['children'].append({
                        'type': 'changed',
                        'key': key,
                        'value1': value1,
                        'children': build_tree({}, value2)['children']
                    })
                else:
                    diff['children'].append({
                        'type': 'changed',
                        'key': key,
                        'value1': value1,
                        'value2': value2
                    })

    return diff
