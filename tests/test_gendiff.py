from gendiff.gendiff import generate_diff
import pytest
from tests import FIXTURES_PATH

FORMATTER_ARGS = [
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


def generate_fixture_path(file_name):
    return f'{FIXTURES_PATH}{file_name}'


def get_expect_result(file):
    with open(file) as expected_result:
        return expected_result.read().strip()


@pytest.mark.parametrize('file1, file2, format_name, output', FORMATTER_ARGS)
def test_run_formatter(file1, file2, format_name, output):
    file1_full_path = generate_fixture_path(file1)
    file2_full_path = generate_fixture_path(file2)
    output_full_path = generate_fixture_path(output)
    assert generate_diff(file1_full_path, file2_full_path, format_name)\
           == get_expect_result(output_full_path)
