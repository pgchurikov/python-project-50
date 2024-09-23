import itertools


def format_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"{value}"
    return str(value)


def do_stylish(value, replacer=' ', spaces_count=2):

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
                        lines.append(
                            f'{deep_indent}+ {key}: '
                            f'{format_value(val["value"])}'
                        )
                    else:
                        lines.append(
                            f'{deep_indent}+ {key}: '
                            f'{iter_(val, deep_indent_size)}'
                        )
                case 'deleted':
                    if 'value' in val:
                        lines.append(
                            f'{deep_indent}- {key}: '
                            f'{format_value(val["value"])}'
                        )
                    else:
                        lines.append(
                            f'{deep_indent}- {key}: '
                            f'{iter_(val, deep_indent_size)}'
                        )
                case 'unchanged':
                    if 'value' in val:
                        lines.append(
                            f'{deep_indent}  {key}: '
                            f'{format_value(val["value"])}'
                        )
                    else:
                        lines.append(
                            f'{deep_indent}  {key}: '
                            f'{iter_(val, deep_indent_size)}'
                        )
                case 'changed':
                    if 'value1' in val and 'value2' in val:
                        lines.append(
                            f'{deep_indent}- {key}: '
                            f'{format_value(val["value1"])}'
                        )
                        lines.append(
                            f'{deep_indent}+ {key}: '
                            f'{format_value(val["value2"])}'
                        )
                    elif 'value1' in val and 'value2' not in val:
                        lines.append(
                            f'{deep_indent}- {key}: '
                            f'{format_value(val["value1"])}'
                        )
                        lines.append(
                            f'{deep_indent}+ {key}: '
                            f'{iter_(val, deep_indent_size)}'
                        )
                    elif 'value1' not in val and 'value2' in val:
                        lines.append(
                            f'{deep_indent}- {key}: '
                            f'{iter_(val, deep_indent_size)}'
                        )
                        lines.append(
                            f'{deep_indent}+ {key}: '
                            f'{format_value(val["value2"])}'
                        )
                case 'nested':
                    lines.append(
                        f'{deep_indent}{key}: {iter_(val, deep_indent_size)}'
                    )

        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
