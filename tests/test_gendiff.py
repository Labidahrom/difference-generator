from gendiff.making_gendiff import generate_diff
import pytest
from tests import FIXTURES_PATH

FORMATTER_ARGUMENTS = [
    ('file1.json', 'file2.json', 'stylish', 'output12.txt'),
    ('file1.yaml', 'file2.yaml', 'stylish', 'output12.txt'),
    ('file3.json', 'file4.json', 'stylish', 'output34.txt'),
    ('file3.yaml', 'file4.yaml', 'stylish', 'output34.txt'),
    ('file1.json', 'file2.json', 'plain', 'output12_plain.txt'),
    ('file1.yaml', 'file2.yaml', 'plain', 'output12_plain.txt'),
    ('file3.json', 'file4.json', 'plain', 'output34_plain.txt'),
    ('file3.yaml', 'file4.yaml', 'plain', 'output34_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'output12_json.txt'),
    ('file1.yaml', 'file2.yaml', 'json', 'output12_json.txt'),
    ('file3.json', 'file4.json', 'json', 'output34_json.txt'),
    ('file3.yaml', 'file4.yaml', 'json', 'output34_json.txt')
]


def make_args(file_names, input_string):
    output = []
    for index in file_names:
        file1 = index[0]
        file2 = index[1]
        input_format = index[2]
        output_file = index[3]
        output.append((f'{input_string}{file1}', f'{input_string}{file2}',
                       input_format, f'{input_string}{output_file}'))
    return output


def get_expect_result(file):
    with open(file) as expected_result:
        return expected_result.read().strip()


@pytest.mark.parametrize('file1, file2, format_name, output',
                         make_args(FORMATTER_ARGUMENTS, FIXTURES_PATH))
def test_run_formatter(file1, file2, format_name, output):
    assert generate_diff(file1, file2, format_name) == get_expect_result(output)
