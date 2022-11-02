from gendiff.scripts.make_gendiff import generate_diff


def get_expected_result(file):
    with open(file) as expected_result:
        return expected_result.read().strip()


def test_generate_diff_with_lesson_data_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == \
           get_expected_result('tests/fixtures/output12.txt')


def test_generate_diff_with_empty_data_json():
    assert generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json') == \
           get_expected_result('tests/fixtures/output34.txt')
    assert generate_diff('tests/fixtures/file5.json', 'tests/fixtures/file6.json') == \
           get_expected_result('tests/fixtures/output56.txt')


def test_generate_diff_with_upper_letters_json():
    assert generate_diff('tests/fixtures/file7.json', 'tests/fixtures/file8.json') == \
           get_expected_result('tests/fixtures/output78.txt')


def test_generate_diff_with_lesson_data_yaml():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == \
           get_expected_result('tests/fixtures/output12.txt')


def test_generate_diff_with_empty_data_yaml():
    assert generate_diff('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml') == \
           get_expected_result('tests/fixtures/output34.txt')
    assert generate_diff('tests/fixtures/file5.yaml', 'tests/fixtures/file6.yaml') == \
           get_expected_result('tests/fixtures/output56.txt')


def test_generate_diff_with_upper_letters_yaml():
    assert generate_diff('tests/fixtures/file7.yaml', 'tests/fixtures/file8.yaml') == \
           get_expected_result('tests/fixtures/output78.txt')