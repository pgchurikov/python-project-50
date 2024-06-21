import argparse
import json


def generate_diff(filepath1, filepath2):
    with open(filepath1) as file1:
        obj1 = json.load(file1)
    with open(filepath2) as file2:
        obj2 = json.load(file2)

    diff = []

    keys = set(obj1.keys()).union(obj2.keys())

    for key in sorted(keys):
        if key not in obj1:
            diff.append(f'+ {key}: {obj2[key]}')
        elif key not in obj2:
            diff.append(f'- {key}: {obj1[key]}')
        elif obj1[key] == obj2[key]:
            diff.append(f'  {key}: {obj1[key]}')
        else:
            diff.append(f'- {key}: {obj1[key]}')
            diff.append(f'+ {key}: {obj2[key]}')

    return '{\n  ' + '\n  '.join(diff) + '\n}'


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
