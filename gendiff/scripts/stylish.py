from gendiff.scripts.create_diff import sort_structure
from gendiff.scripts.create_diff import replace_value
from gendiff.scripts.create_diff import get_sign
from gendiff.scripts.create_diff import change_sign


def make_stylish(data, level=4):
    if not data:
        return ''
    output = '{\n'
    for i in data:
        if not isinstance(i['children'], list):
            output += f'{get_sign(i, " " * level)}{i["key"]}: {i["value"]}\n'
        else:
            output += f'{get_sign(i, " " * level)}{i["key"]}: {i["value"]}'
            output += make_stylish(i['children'], level + 4)
    output += (f'{" " * (level - 4)}' + '}\n')
    return output


def make_stylish_data(data):
    change_sign(data)
    sort_structure(data)
    output = make_stylish(data)
    output = replace_value(output)
    return output
