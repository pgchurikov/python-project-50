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
        if key.startswith('  - '):
            key = key[4:]
            current_path = f"{path}.{key}".strip('.')
            if f'  + {key}' in diff:
                updated_value = diff[f'  + {key}']
                lines.append(
                    f"Property '{current_path}' was updated. "
                    f"From {format_value(value)} "
                    f"to {format_value(updated_value)}"
                )
            else:
                lines.append(f"Property '{current_path}' was removed")
        elif key.startswith('  + '):
            key = key[4:]
            current_path = f"{path}.{key}".strip('.')
            if f'  - {key}' not in diff:
                lines.append(
                    f"Property '{current_path}' "
                    f"was added with value: {format_value(value)}"
                )
        else:
            if isinstance(value, dict):
                lines.extend(build_plain(value, f"{path}.{key}".strip('.')))

    return sorted(lines)


def plain(diff):
    return '\n'.join(build_plain(diff))
