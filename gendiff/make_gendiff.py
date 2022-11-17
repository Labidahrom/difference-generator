from gendiff.parser import get_data
from gendiff.create_diff import make_diff_data
from gendiff.formatters.stylish import make_stylish_data
from gendiff.formatters.plain import make_plain_data
from gendiff.formatters.json_m import make_json_data


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    data = make_diff_data(file1, file2)
    if format_name == "plain":
        output = make_plain_data(data)
        print(output)
        return output
    elif format_name == 'json':
        output = make_json_data(data)
        print(output)
        return output
    else:
        output = make_stylish_data(data)
        print(output)
        return output
