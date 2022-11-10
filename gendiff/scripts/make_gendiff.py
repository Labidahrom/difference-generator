from gendiff.scripts.parser import get_data
from gendiff.scripts.create_diff import make_diff_data
from gendiff.scripts.stylish import make_stylish_data


def generate_diff(file1, file2):
    file1 = get_data(file1)
    file2 = get_data(file2)
    data = make_diff_data(file1, file2)
    output = make_stylish_data(data)
    print(output)
    return output
