def add_stylish_start(key):
    if key['parent'] == 'added':
        output = '  + '
    elif key['parent'] == 'removed':
        output = '  - '
    else:
        output = '    '
    return output


def make_stylish_nested_value(data, level):
    output = []
    if isinstance(data, dict):
        output.append('{\n')
        for i in data:
            if not isinstance(data[i], dict):
                output.append(f'{" " * level}    {i}: {data[i]}\n')
            else:
                output.append(f'{" " * level}    {i}: ')
                output.append(make_stylish_nested_value(data[i], level + 4))
        output.append((level * ' ') + '}' + '\n')
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return str(data)
    return ''.join(output)


def make_stylish(data, level=0):
    output = ['{\n']
    for i in data:
        if i.get('action') == 'nested':
            if i['parent'] == 'same':
                output.append(f'{" " * level}{add_stylish_start(i)}'
                              f'{i["key"]}: ')
                output.append(make_stylish(i['children'], level + 4))
            else:
                output.append(f'{" " * level}{add_stylish_start(i)}'
                              f'{i["key"]}: ')
                output.append(make_stylish_nested_value(i['value'],
                                                        level + 4))
        else:
            output.append(f'{" " * level}{add_stylish_start(i)}{i["key"]}:'
                          f' {make_stylish_nested_value(i["value"], level)}\n')
    output.append((level * ' ') + '}' + '\n')
    return ''.join(output)


def render_to_stylish(data):
    output = make_stylish(data)
    return output.strip()
