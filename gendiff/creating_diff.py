def take_item_for_sort(item):
    sort_dict = {'same': '1', 'removed': '2', 'added': '3'}
    return str(item['key']) + str(sort_dict[(item['action'])])


def sort_structure(list_):
    for i in list_:
        if isinstance(i['children'], list):
            sort_structure(i['children'])
    list_.sort(key=take_item_for_sort)


def get_sign(item, string):
    if item['action'] == 'removed':
        return f'{string[:-2]}-{string[-1]}'
    elif item['action'] == 'added':
        return f'{string[:-2]}+{string[-1]}'
    else:
        return string


def get_index(item, given_list):
    return given_list.index(item)


def make_children_unsigned(tree):
    for i in range(len(tree['children'])):
        tree['children'][i]['action'] = 'same'


def has_sighned_children(item):
    if item['children']:
        for i in item['children']:
            if i['action'] != 'same':
                return True
        return False


def change_sign(tree):
    for i in tree:
        if has_sighned_children(i) and i['children']:
            change_sign(i['children'])
            if i['action'] != 'same' and has_sighned_children(i):
                make_children_unsigned(tree[get_index(i, tree)])


def make_entry(key, value, level, children, action):
    new_dict = {
        'key': key,
        'value': value,
        'level': level,
        'children': children,
        'action': action
    }
    return new_dict


def make_list_entry(item, action, level=1):
    new_list = []
    for key, value in item.items():
        if not isinstance(value, dict):
            new_dict = make_entry(key, value, level, '', action)
        else:
            new_dict = \
                make_entry(key, '', level,
                           make_list_entry(value, action, level + 1), action)
        new_list.append(new_dict)
    return new_list


def make_complex_entry(key, value, level, action):
    if not isinstance(value, dict):
        new_dict = make_entry(key, value, level, '', action)
    else:
        new_dict = make_entry(key, '', level,
                              make_list_entry(value, action, level + 1),
                              action)
    return new_dict


def merge_data(content1, content2, level=0):
    new_list = []
    for key, value in content1.items():
        if key not in content2:
            new_list.append(make_complex_entry(key, value, level, 'removed'))
        elif key in content2 and content2[key] == value:
            new_list.append(make_complex_entry(key, value, level, 'same'))
            content2.pop(key)
        elif key in content2 and content2[key] != value:
            if isinstance(value, dict) and isinstance(content2[key], dict):
                new_list.append(make_entry
                                (key, '', level, merge_data
                                    (value, content2[key], level + 1), 'same'))
            else:
                new_list.append(make_complex_entry
                                (key, value, level, 'removed'))
                new_list.append(make_complex_entry
                                (key, content2[key], level, 'added'))
            content2.pop(key)
    new_list.extend(make_list_entry(content2, 'added', level))
    return new_list


def make_diff_data(content1, content2):
    merged_data = merge_data(content1, content2)
    return merged_data
