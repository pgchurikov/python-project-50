from gendiff.parcer import read_file
from gendiff.formatter import stylish
from gendiff.fromat_plain import plain


def generate_diff(file_path1, file_path2, format=stylish):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_tree(data1, data2)

    formatters = {
        'stylish': stylish,
        'plain': plain,
    }

    return formatters[format](diff)


def build_tree(data1, data2):
    diff = {}
    all_keys = sorted(data1.keys() | data2.keys())
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff[f'    {key}'] = value1
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = build_tree(value1, value2)
        else:
            if key in data1:
                diff[f'  - {key}'] = value1
            if key in data2:
                diff[f'  + {key}'] = value2

    return diff
