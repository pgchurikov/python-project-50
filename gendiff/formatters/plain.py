def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def build_plain(diff, path=''):
    lines = []

    for item in diff:
        key = item['key']
        current_path = f"{path}.{key}".strip('.')

        if item['type'] == 'deleted':
            lines.append(get_removal(current_path))
        elif item['type'] == 'added':
            lines.append(get_addition(item['value'], current_path))
        elif item['type'] == 'changed':
            lines.append(get_change(item, current_path))
        elif item['type'] == 'nested':
            lines.extend(build_plain(item['value'], current_path))

    return sorted(filter(None, lines))


def get_removal(current_path):
    return f"Property '{current_path}' was removed"


def get_addition(value, current_path):
    return (
        f"Property '{current_path}' "
        f"was added with value: {format_value(value)}"
    )


def get_change(change_item, current_path):
    value1 = change_item['value1']
    value2 = change_item['value2']
    return (
        f"Property '{current_path}' was updated. "
        f"From {format_value(value1)} "
        f"to {format_value(value2)}"
    )


def do_plain(diff):
    return '\n'.join(build_plain(diff))
