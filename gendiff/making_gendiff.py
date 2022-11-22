from gendiff.parser import get_data
from gendiff.creating_diff import make_diff_data
from gendiff.formatters import make_format_data


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    data = make_diff_data(file1, file2)
    formatted_data = make_format_data(data, format_name)
    return formatted_data
