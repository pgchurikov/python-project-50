def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def to_str(data, depth):
    if isinstance(data, bool):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    if isinstance(data, dict):
        parts = []
        for key in data:
            indent = build_indent(depth + 1)
            formatted_value = to_str(data[key], depth + 1)
            parts.append(f"{indent}  {key}: {formatted_value}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"

    return data


def stylish(diff):

    def iter_(node, depth=0):
        children = node.get('children')
        indent = build_indent(depth)
        formatted_value = to_str(node.get('value'), depth)
        formatted_value1 = to_str(node.get('value1'), depth)
        formatted_value2 = to_str(node.get('value2'), depth)

        if node['type'] == 'root':
            lines = map(lambda child: iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f'{{\n{result}\n}}'

        if node['type'] == 'nested':
            lines = map(lambda child: iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f"{indent}  {node['key']}: {{\n{result}\n{indent}  }}"

        if node['type'] == 'added':
            return f"{indent}+ {node['key']}: {formatted_value}"

        if node['type'] == 'deleted':
            return f"{indent}- {node['key']}: {formatted_value}"

        if node['type'] == 'changed':
            lines = [
                f"{indent}- {node['key']}: {formatted_value1}",
                f"{indent}+ {node['key']}: {formatted_value2}"
            ]
            return '\n'.join(lines)

        if node['type'] == 'unchanged':
            return f"{indent}  {node['key']}: {formatted_value}"

        raise ValueError(f"Unknown type: {node['type']}")

    return iter_(diff)
