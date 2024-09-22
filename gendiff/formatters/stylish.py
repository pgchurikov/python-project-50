import itertools


def do_stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for val in current_value.get('children', []):
            key = val['key']
            match val['type']:
                case 'added':
                    if 'value' in val:
                        lines.append(f'{deep_indent}+ {key}: {val["value"]}')
                case 'deleted':
                    if 'value' in val:
                        lines.append(f'{deep_indent}- {key}: {val["value"]}')
                case 'unchanged':
                    if 'value' in val:
                        lines.append(f'{deep_indent}  {key}: {val["value"]}')
                case 'changed':
                    if 'value1' in val and 'value2' in val:
                        lines.append(f'{deep_indent}- {key}: {val["value1"]}')
                        lines.append(f'{deep_indent}+ {key}: {val["value2"]}')
                case 'nested':
                    lines.append(
                        f'{deep_indent}{key}: {iter_(val, deep_indent_size)}'
                    )

        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
