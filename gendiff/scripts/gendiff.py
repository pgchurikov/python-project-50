#!/usr/bin/env python3


from gendiff.gendiff_help import parse_args
from gendiff.build_diff import generate_diff


def main():
    path1, path2 = parse_args()

    diff = generate_diff(path1, path2)
    print(diff)


if __name__ == '__main__':
    main()
