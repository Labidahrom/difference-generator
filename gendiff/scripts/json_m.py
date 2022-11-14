from gendiff.scripts.create_diff import sort_structure
from gendiff.scripts.create_diff import replace_value


def define_str_value(item):
    if isinstance(item['value'], str):
        return f'"{item["value"]}"'
    else:
        return item['value']


def define_comma(item, tree):
    if tree.index(item) < (len(tree) - 1):
        return ','
    else:
        return ''


def make_json(data, level=2):
    if not data:
        return ''
    output = '{\n'
    for i in data:
        if not isinstance(i['children'], list) and i['file'] == 'file2':
            output += f'{" " * level}"{i["key"]}": {define_str_value(i)}' \
                      f'{define_comma(i, data)}\n'
        elif isinstance(i['children'], list) and i['file'] != 'file1':
            output += f'{" " * level}"{i["key"]}": '
            output += (make_json(i['children'],
                                 level + 2) + define_comma(i, data) + '\n')
    output += (f'{" " * (level - 2)}' + '}')
    return output


def make_json_data(data):
    sort_structure(data)
    output = make_json(data)
    output = replace_value(output)
    return output
