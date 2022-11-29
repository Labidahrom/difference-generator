def replace_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def add_stylish_start(key):
    if key['action'] == 'added':
        output = '  + '
    elif key['action'] == 'removed':
        output = '  - '
    else:
        output = '    '
    return output


def make_stylish_nested_value(data, level):
    output = '{\n'
    for i in data:
        if not isinstance(data[i], dict):
            output += f'{" " * level}    {i}: {replace_value(data[i])}\n'
        else:
            output += f'{" " * level}    {i}: '
            output += make_stylish_nested_value(data[i], level + 4)
    output += ((level * ' ') + '}' + '\n')
    return output


def make_stylish(data, level=0):
    output = '{\n'
    for i in data:
        if isinstance(i['children'], list):
            output += f'{" " * level}{add_stylish_start(i)}{i["key"]}: '
            output += make_stylish(i['children'], level + 4)
        elif isinstance(i['value'], dict):
            output += f'{" " * level}{add_stylish_start(i)}{i["key"]}: '
            output += make_stylish_nested_value(i['value'], level + 4)
        else:
            output += f'{" " * level}{add_stylish_start(i)}{i["key"]}: ' \
                      f'{replace_value(i["value"])}\n'
    output += ((level * ' ') + '}' + '\n')
    return output


def make_stylish_data(data):
    output = make_stylish(data).strip()
    return output
