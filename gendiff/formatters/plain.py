def replace_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def define_value(item):
    if isinstance(item, dict):
        return '[complex value]'
    else:
        if isinstance(item, str):
            return f"'{item}'"
        else:
            return replace_value(item)


def make_plain(tree, path=''):
    output = []
    for item in tree:
        if item['parent'] == 'removed' and item['old_value']\
                == 'not_duplicated':
            output.append(f"Property '{path + item['key']}' was removed")
        elif item['parent'] == 'added' and item['old_value']\
                != 'not_duplicated':
            output.append(f"Property '{path + item['key']}' was updated. "
                          f"From {define_value(item['old_value'])} to "
                          f"{define_value(item['value'])}")
        elif item['parent'] == 'added' and item['old_value'] \
                == 'not_duplicated':
            output.append(f"Property '{path + item['key']}'"
                          f" was added with value: "
                          f"{define_value(item['value'])}")
        elif item['parent'] == 'same' and item['children']:
            output.append(make_plain(item['children'],
                                     path=path + item['key'] + '.'))
    return '\n'.join(output)


def render_to_plain(data):
    output = make_plain(data)
    return output
