import json
import yaml


def read_file(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        # Заменяем булевы значения в строке
        data = data.replace('true', '"true"').replace('false', '"false"')
        if str(filepath[-1:-4]) == 'json':
            return json.loads(data)
        if str(filepath[-1:-4]) == 'yaml':
            return yaml.safe_load(data)
        if str(filepath[-1:-3]) == 'yml':
            return yaml.safe_load(data)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = ''
    for key in sorted(data1.keys() | data2.keys()):
        if key in data1 and key not in data2:
            diff += f'  - {key}: {data1[key]}\n'
        elif key in data2 and key not in data1:
            diff += f'  + {key}: {data2[key]}\n'
        elif data1[key] == data2[key]:
            diff += f'    {key}: {data1[key]}\n'
        else:
            diff += f'  - {key}: {data1[key]}\n  + {key}: {data2[key]}\n'

    result = '{\n' + diff + '}'
    return result
