from gendiff.make_gendiff import generate_diff
import pytest
from tests import FIXTURES_PATH


FORMATTER_ARGUMENTS = [
    (f'{FIXTURES_PATH}file1.json', f'{FIXTURES_PATH}file2.json',
     'stylish', f'{FIXTURES_PATH}output12.txt'),
    (f'{FIXTURES_PATH}file1.yaml', f'{FIXTURES_PATH}file2.yaml',
     'stylish', f'{FIXTURES_PATH}output12.txt'),
    (f'{FIXTURES_PATH}file3.json', f'{FIXTURES_PATH}file4.json',
     'stylish', f'{FIXTURES_PATH}output34.txt'),
    (f'{FIXTURES_PATH}file3.yaml', f'{FIXTURES_PATH}file4.yaml',
     'stylish', f'{FIXTURES_PATH}output34.txt'),
    (f'{FIXTURES_PATH}file5.json', f'{FIXTURES_PATH}file6.json',
     'stylish', f'{FIXTURES_PATH}output56.txt'),
    (f'{FIXTURES_PATH}file5.yaml', f'{FIXTURES_PATH}file6.yaml',
     'stylish', f'{FIXTURES_PATH}output56.txt'),
    (f'{FIXTURES_PATH}file7.json', f'{FIXTURES_PATH}file8.json',
     'stylish', f'{FIXTURES_PATH}output78.txt'),
    (f'{FIXTURES_PATH}file7.yaml', f'{FIXTURES_PATH}file8.yaml',
     'stylish', f'{FIXTURES_PATH}output78.txt'),
    (f'{FIXTURES_PATH}file1.json', f'{FIXTURES_PATH}file2.json',
     'plain', f'{FIXTURES_PATH}output12_plain.txt'),
    (f'{FIXTURES_PATH}file1.yaml', f'{FIXTURES_PATH}file2.yaml',
     'plain', f'{FIXTURES_PATH}output12_plain.txt'),
    (f'{FIXTURES_PATH}file3.json', f'{FIXTURES_PATH}file4.json',
     'plain', f'{FIXTURES_PATH}output34_plain.txt'),
    (f'{FIXTURES_PATH}file3.yaml', f'{FIXTURES_PATH}file4.yaml',
     'plain', f'{FIXTURES_PATH}output34_plain.txt'),
    (f'{FIXTURES_PATH}file5.json', f'{FIXTURES_PATH}file6.json',
     'plain', f'{FIXTURES_PATH}output56_plain.txt'),
    (f'{FIXTURES_PATH}file5.yaml', f'{FIXTURES_PATH}file6.yaml',
     'plain', f'{FIXTURES_PATH}output56_plain.txt'),
    (f'{FIXTURES_PATH}file7.json', f'{FIXTURES_PATH}file8.json',
     'plain', f'{FIXTURES_PATH}output78_plain.txt'),
    (f'{FIXTURES_PATH}file7.yaml', f'{FIXTURES_PATH}file8.yaml',
     'plain', f'{FIXTURES_PATH}output78_plain.txt'),
    (f'{FIXTURES_PATH}file1.json', f'{FIXTURES_PATH}file2.json',
     'json', f'{FIXTURES_PATH}output12_json.txt'),
    (f'{FIXTURES_PATH}file1.yaml', f'{FIXTURES_PATH}file2.yaml',
     'json', f'{FIXTURES_PATH}output12_json.txt'),
    (f'{FIXTURES_PATH}file3.json', f'{FIXTURES_PATH}file4.json',
     'json', f'{FIXTURES_PATH}output34_json.txt'),
    (f'{FIXTURES_PATH}file3.yaml', f'{FIXTURES_PATH}file4.yaml',
     'json', f'{FIXTURES_PATH}output34_json.txt'),
    (f'{FIXTURES_PATH}file5.json', f'{FIXTURES_PATH}file6.json',
     'json', f'{FIXTURES_PATH}output56_json.txt'),
    (f'{FIXTURES_PATH}file5.yaml', f'{FIXTURES_PATH}file6.yaml',
     'json', f'{FIXTURES_PATH}output56_json.txt'),
    (f'{FIXTURES_PATH}file7.json', f'{FIXTURES_PATH}file8.json',
     'json', f'{FIXTURES_PATH}output78_json.txt'),
    (f'{FIXTURES_PATH}file7.yaml', f'{FIXTURES_PATH}file8.yaml',
     'json', f'{FIXTURES_PATH}output78_json.txt')
]


def get_expect_result(file):
    with open(file) as expected_result:
        return expected_result.read().strip()


@pytest.mark.parametrize('file1, file2, format_name, output',
                         FORMATTER_ARGUMENTS)
def test_run_formatter(file1, file2, format_name, output):
    assert generate_diff(file1, file2, format_name) == get_expect_result(output)
