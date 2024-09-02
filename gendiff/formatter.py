import itertools


def stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if key.startswith(('  - ', '  + ', '    ')):
                lines.append(
                    f'{current_indent}{key}: {iter_(val, deep_indent_size)}'
                    )
            else:
                lines.append(
                    f'{deep_indent}{key}: {iter_(val, deep_indent_size)}'
                    )
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
