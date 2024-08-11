#!/usr/bin/env python3


from gendiff.gendiff_help import help
from gendiff.build_diff import generate_diff


def main():
    print(help())
    path1, path2 = help.args
    print(generate_diff(path1, path2))


if __name__ == '__main__':
    main()
