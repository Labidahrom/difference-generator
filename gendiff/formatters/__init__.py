from gendiff.formatters.json_m import render_to_json
from gendiff.formatters.plain import render_to_plain
from gendiff.formatters.stylish import render_to_stylish


def apply_format(data, format_name):
    if format_name == "plain":
        return render_to_plain(data)
    elif format_name == 'json':
        return render_to_json(data)
    elif format_name == 'stylish':
        return render_to_stylish(data)
    raise Exception('This format type is not supported')
