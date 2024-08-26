def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value == 'true':
        return 'true'
    elif value == 'false':
        return 'false'
    elif value == 'null':
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def build_plain(diff, path=''):
    lines = []

    for key, value in sorted(diff.items()):
        base_key = key[4:] if key.startswith(('  - ', '  + ')) else key
        current_path = f"{path}.{base_key}".strip('.')

        if key.startswith('  - '):
            lines.append(get_removal(key, value, diff, current_path))
        elif key.startswith('  + '):
            lines.append(get_addition(key, diff, current_path))
        elif isinstance(value, dict):
            lines.extend(build_plain(value, current_path))

    return sorted(filter(None, lines))


def get_removal(key, value, diff, current_path):
    base_key = key[4:]
    if f'  + {base_key}' in diff:
        updated_value = diff[f'  + {base_key}']
        return (
            f"Property '{current_path}' was updated. "
            f"From {format_value(value)} "
            f"to {format_value(updated_value)}"
        )
    return f"Property '{current_path}' was removed"


def get_addition(key, diff, current_path):
    base_key = key[4:]
    if f'  - {base_key}' not in diff:
        return (
            f"Property '{current_path}' "
            f"was added with value: {format_value(diff[key])}"
        )


def plain(diff):
    return '\n'.join(build_plain(diff))
