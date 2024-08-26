#!/usr/bin/env python3


from gendiff.gendiff_help import help
from gendiff.build_diff import generate_diff


def main():
    file_path1, file_path2, format = help()
    diff = (generate_diff(file_path1, file_path2, format))
    print(diff)


if __name__ == '__main__':
    main()
