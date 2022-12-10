prefix_map = {
    'added': '  + ',
    'removed': '  - ',
    'updated': '  - ',
    'same': '    ',
    'nested': '    '
}


def make_stylish_nested_value(data, level):
    output = ['{\n']
    if isinstance(data, dict):
        for i in data:
            if not isinstance(data[i], dict):
                output.append(f'{" " * level}    {i}: {data[i]}' + '\n')
            else:
                output.append(f'{" " * level}    {i}: ')
                output.append(make_stylish_nested_value(data[i], level + 4)
                              + '\n')
        output.append((level * ' ') + '}')
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
        if i['action'] == 'nested':
            output.append(f'{" " * level}{prefix_map[i["action"]]}'
                          f'{i["key"]}: ')
            output.append(make_stylish(i['children'], level + 4))
        else:
            output.append(f'{" " * level}{prefix_map[i["action"]]}{i["key"]}:'
                          f' {make_stylish_nested_value(i["value"], level+4)}'
                          f'\n')
    output.append((level * ' ') + '}' + '\n')
    return ''.join(output)


def render_to_stylish(data):
    output = make_stylish(data)
    return output.strip()
