from gendiff.parser import get_data
from gendiff.dicts_diff import build_diff
from gendiff.formatters import make_format_data


def generate_diff(file1, file2, format_name='stylish'):
    content1 = get_data(file1)
    content2 = get_data(file2)
    data = build_diff(content1, content2)
    return make_format_data(data, format_name)
