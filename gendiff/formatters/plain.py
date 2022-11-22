from gendiff.creating_diff import sort_structure
from gendiff.creating_diff import change_sign


def get_same_item(tree, key, value):
    for i in tree:
        if i['key'] == key and i['value'] != value:
            return i


def define_value(item):
    if item['children']:
        return '[complex value]'
    else:
        if isinstance(item['value'], str):
            return f"'{item['value']}'"
        else:
            return item['value']


def make_plain(tree, path=''):
    output = ''
    for item in tree:
        if get_same_item(tree, item['key'], item['value']):
            update_item = get_same_item(tree, item['key'], item['value'])
            string = f"Property '{path + item['key']}' was updated. " \
                     f"From {define_value(item)} to " \
                     f"{define_value(update_item)}\n"
            output += string
            tree.remove(update_item)
        else:
            if item['children'] and item['action'] == 'same':
                output += make_plain(item['children'],
                                     path=path + item['key'] + '.')
            elif item['action'] == 'removed':
                string = f"Property '{path + item['key']}' was removed\n"
                output += string
            elif item['action'] == 'added':
                string = f"Property '{path + item['key']}' " \
                         f"was added with value: " \
                         f"{define_value(item)}\n"
                output += string
    return output


def make_plain_data(data):
    change_sign(data)
    sort_structure(data)
    output = make_plain(data)
    return output
