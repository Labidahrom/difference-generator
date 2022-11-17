from gendiff.make_gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
STYLISH_FORMATTER_DATA = \
    [(f'{PATH}file1.json', f'{PATH}file2.json', f'{PATH}output12.txt'),
     (f'{PATH}file1.yaml', f'{PATH}file2.yaml', f'{PATH}output12.txt'),
     (f'{PATH}file3.json', f'{PATH}file4.json', f'{PATH}output34.txt'),
     (f'{PATH}file3.yaml', f'{PATH}file4.yaml', f'{PATH}output34.txt'),
     (f'{PATH}file5.json', f'{PATH}file6.json', f'{PATH}output56.txt'),
     (f'{PATH}file5.yaml', f'{PATH}file6.yaml', f'{PATH}output56.txt'),
     (f'{PATH}file7.json', f'{PATH}file8.json', f'{PATH}output78.txt'),
     (f'{PATH}file7.yaml', f'{PATH}file8.yaml', f'{PATH}output78.txt')]
PLAIN_FORMATTER_DATA = \
    [(f'{PATH}file1.json', f'{PATH}file2.json', f'{PATH}output12_plain.txt'),
     (f'{PATH}file1.yaml', f'{PATH}file2.yaml', f'{PATH}output12_plain.txt'),
     (f'{PATH}file3.json', f'{PATH}file4.json', f'{PATH}output34_plain.txt'),
     (f'{PATH}file3.yaml', f'{PATH}file4.yaml', f'{PATH}output34_plain.txt'),
     (f'{PATH}file5.json', f'{PATH}file6.json', f'{PATH}output56_plain.txt'),
     (f'{PATH}file5.yaml', f'{PATH}file6.yaml', f'{PATH}output56_plain.txt'),
     (f'{PATH}file7.json', f'{PATH}file8.json', f'{PATH}output78_plain.txt'),
     (f'{PATH}file7.yaml', f'{PATH}file8.yaml', f'{PATH}output78_plain.txt')]
JSON_FORMATTER_DATA = \
    [(f'{PATH}file1.json', f'{PATH}file2.json', f'{PATH}output12_json.txt'),
     (f'{PATH}file1.yaml', f'{PATH}file2.yaml', f'{PATH}output12_json.txt'),
     (f'{PATH}file3.json', f'{PATH}file4.json', f'{PATH}output34_json.txt'),
     (f'{PATH}file3.yaml', f'{PATH}file4.yaml', f'{PATH}output34_json.txt'),
     (f'{PATH}file5.json', f'{PATH}file6.json', f'{PATH}output56_json.txt'),
     (f'{PATH}file5.yaml', f'{PATH}file6.yaml', f'{PATH}output56_json.txt'),
     (f'{PATH}file7.json', f'{PATH}file8.json', f'{PATH}output78_json.txt'),
     (f'{PATH}file7.yaml', f'{PATH}file8.yaml', f'{PATH}output78_json.txt')]


def get_expect_result(file):
    with open(file) as expected_result:
        return expected_result.read().strip()


@pytest.mark.parametrize('file1,file2,output', STYLISH_FORMATTER_DATA)
def test_stylish_formatter(file1, file2, output):
    assert generate_diff(file1, file2) == get_expect_result(output)


@pytest.mark.parametrize('file1,file2,output', PLAIN_FORMATTER_DATA)
def test_plain_formatter(file1, file2, output):
    assert generate_diff(file1, file2, 'plain') == get_expect_result(output)


@pytest.mark.parametrize('file1,file2,output', JSON_FORMATTER_DATA)
def test_json_formatter(file1, file2, output):
    assert generate_diff(file1, file2, 'json') == get_expect_result(output)
