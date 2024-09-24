import itertools


def format_dict(value, indent):
    current_indent = ' ' * (indent * 2)
    formatted_dict = []
    for k, v in value.items():
        formatted_dict.append(
            f"{current_indent}{k}: {format_value(v, indent + 1)}"
        )
    return "\n".join(formatted_dict)


def format_value(value, indent=1):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"{value}"
    elif isinstance(value, dict):
        return f"{{\n{format_dict(value, indent)}\n{' ' * (indent - 1) * 2}}}"
    return str(value)


def do_stylish(value, replacer=' ', spaces_count=2):

    def iter_(current_value, depth):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for val in current_value:
            key = val['key']
            match val['type']:
                case 'added':
                    lines.append(
                        f'{deep_indent}+ {key}: '
                        f'{format_value(val["value"], deep_indent_size)}'
                    )
                case 'deleted':
                    lines.append(
                        f'{deep_indent}- {key}: '
                        f'{format_value(val["value"], deep_indent_size)}'
                    )
                case 'unchanged':
                    lines.append(
                        f'{deep_indent}  {key}: '
                        f'{format_value(val["value"], deep_indent_size)}'
                    )
                case 'changed':
                    lines.append(
                        f'{deep_indent}- {key}: '
                        f'{format_value(val["value1"], deep_indent_size)}'
                    )
                    lines.append(
                        f'{deep_indent}+ {key}: '
                        f'{format_value(val["value2"], deep_indent_size)}'
                    )
                case 'nested':
                    lines.append(
                        f'{deep_indent}  {key}: '
                        f'{iter_(val["value"], deep_indent_size)}'
                    )

        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
