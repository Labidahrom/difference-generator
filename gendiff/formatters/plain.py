def define_value(item):
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, str):
        return f"'{item}'"
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'


def make_plain(tree, path=''):
    output = []
    for item in tree:
        if item['action'] == 'removed':
            output.append(f"Property '{path + item['key']}' was removed")
        elif item['action'] == 'added' and item['old_value'] != 'no':
            output.append(f"Property '{path + item['key']}' was updated. "
                          f"From {define_value(item['old_value'])} to "
                          f"{define_value(item['value'])}")
        elif item['action'] == 'added':
            output.append(f"Property '{path + item['key']}'"
                          f" was added with value: "
                          f"{define_value(item['value'])}")
        elif item['action'] == 'nested' and item['children']:
            output.append(make_plain(item['children'],
                                     path=path + item['key'] + '.'))
    return '\n'.join(output)


def render_to_plain(data):
    output = make_plain(data)
    return output
