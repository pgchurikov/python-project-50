from gendiff.parcer import read_file
from gendiff.formatter import stylish


def generate_diff(file_path1, file_path2, formatter=stylish):
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
    return formatter(result)
