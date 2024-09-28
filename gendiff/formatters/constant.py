from gendiff.formatters.stylish import do_stylish
from gendiff.formatters.plain import do_plain
from gendiff.formatters.json import do_json


FORMATTERS = {
    'stylish': do_stylish,
    'plain': do_plain,
    'json': do_json
}
