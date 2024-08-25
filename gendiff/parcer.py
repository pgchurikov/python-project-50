import json
import yaml
import os


def read_file(filepath):
    _, extension = os.path.splitext(filepath)
    extension = extension.lower()
    with open(filepath, 'r') as file:
        data = file.read()
        # Заменяем булевы значения в строке
        data = data.replace('true', '"true"').replace('false', '"false"')
        data = data.replace('null', '"null"')
        if extension == '.json':
            return json.loads(data)
        if extension == '.yaml':
            return yaml.safe_load(data)
        if extension == '.yml':
            return yaml.safe_load(data)
