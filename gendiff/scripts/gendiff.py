import argparse
import json


def read_file(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        # Заменяем булевы значения в строке
        data = data.replace('true', '"true"').replace('false', '"false"')
        return json.loads(data)


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


def main():
    parser = argparse.ArgumentParser(description='Compares '
                                                 'two configuration files'
                                                 ' and shows a difference.')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', help='Set format of output')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
