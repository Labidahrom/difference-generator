def take_item_for_sort(item):
    return str(item['key']) + str(item['file'])


def sort_structure(list_):
    for i in list_:
        if isinstance(i['children'], list):
            sort_structure(i['children'])
    list_.sort(key=take_item_for_sort)


def get_sign(item, string):
    if item['file'] == 'file1':
        return f'{string[:-2]}-{string[-1]}'
    elif item['file'] == 'file2':
        return f'{string[:-2]}+{string[-1]}'
    else:
        return string


def replace_value(string):
    return string.replace('None', 'null').replace('True', 'true').\
        replace('False', 'false').strip()


def make_stylish_string(data, level=4):
    if not data:
        return ''
    output = '{\n'
    for i in data:
        if not isinstance(i['children'], list):
            output += f'{get_sign(i, " " * level)}{i["key"]}: {i["value"]}\n'
        else:
            output += f'{get_sign(i, " " * level)}{i["key"]}: {i["value"]}'
            output += make_stylish_string(i['children'], level + 4)
    output += (f'{" " * (level - 4)}' + '}\n')
    output = output.replace('None', 'null').replace('True', 'true').\
        replace('False', 'false')
    return output


def make_stylish_data(data):
    sort_structure(data)
    output = make_stylish_string(data)
    output = replace_value(output)
    return output
