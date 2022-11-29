from gendiff.formatters.json_m import make_json_data
from gendiff.formatters.plain import make_plain_data
from gendiff.formatters.stylish import make_stylish_data


def replace_value(string):
    return string.replace('None', 'null').replace('True', 'true'). \
        replace('False', 'false').strip()


def make_format_data(data, format_name):
    if format_name == "plain":
        output = make_plain_data(data)
    elif format_name == 'json':
        output = make_json_data(data)
    elif format_name == 'stylish':
        output = make_stylish_data(data)
    else:
        raise Exception('This format type is not supported')
    return output
