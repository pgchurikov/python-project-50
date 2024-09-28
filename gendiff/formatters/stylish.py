import itertools


def format_dict(value, depth):
    formatted_dict = []
    for k, v in value.items():
        formatted_dict.append(
            f"{' ' * (depth * 2 + 2)}{k}: {format_value(v, depth + 2)}"
        )
    return "\n".join(formatted_dict)


def format_value(value, depth=0):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    elif isinstance(value, dict):
        return f"{{\n{format_dict(value, depth)}\n{' ' * ((depth - 1) * 2)}}}"
    return str(value)


def do_stylish(value, replacer=' ', spaces_count=2):
    def iter_(current_value, depth):
        deep_indent_size = depth * spaces_count
        deep_indent = replacer * deep_indent_size
        lines = []
        for val in current_value:
            key = val['key']
            match val['type']:
                case 'added':
                    lines.append(
                        f'{deep_indent}+ {key}: '
                        f'{format_value(val["value"], depth + 2)}'
                    )
                case 'deleted':
                    lines.append(
                        f'{deep_indent}- {key}: '
                        f'{format_value(val["value"], depth + 2)}'
                    )
                case 'unchanged':
                    lines.append(
                        f'{deep_indent}  {key}: '
                        f'{format_value(val["value"], depth + 2)}'
                    )
                case 'changed':
                    lines.append(
                        f'{deep_indent}- {key}: '
                        f'{format_value(val["value1"], depth + 2)}'
                    )
                    lines.append(
                        f'{deep_indent}+ {key}: '
                        f'{format_value(val["value2"], depth + 2)}'
                    )
                case 'nested':
                    lines.append(
                        f'{deep_indent}  {key}: '
                        f'{iter_(val["value"], depth + 2)}'
                    )

        result = itertools.chain(
            ["{"], lines, [f"{' ' * ((depth - 1) * 2)}}}"]
            )
        return '\n'.join(result)

    return iter_(value, 1)
