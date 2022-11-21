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


def get_index(item, given_list):
    return given_list.index(item)


def replace_value(string):
    return string.replace('None', 'null').replace('True', 'true'). \
        replace('False', 'false').strip()


def make_children_unsigned(tree):
    for i in range(len(tree['children'])):
        tree['children'][i]['file'] = 'both'


def has_sighned_children(item):
    if item['children']:
        for i in item['children']:
            if i['file'] != 'both':
                return True
        return False


def change_sign(tree):
    for i in tree:
        if has_sighned_children(i) and i['children']:
            change_sign(i['children'])
            if i['file'] != 'both' and has_sighned_children(i):
                make_children_unsigned(tree[get_index(i, tree)])


def make_entry(key, value, level, children, file):
    new_dict = {
        'key': key,
        'value': value,
        'level': level,
        'children': children,
        'file': file
    }
    return new_dict


def make_list_entry(item, file, level=1):
    new_list = []
    for key, value in item.items():
        if not isinstance(value, dict):
            new_dict = make_entry(key, value, level, '', file)
        else:
            new_dict = \
                make_entry(key, '', level,
                           make_list_entry(value, file, level + 1), file)
        new_list.append(new_dict)
    return new_list


def make_complex_entry(key, value, level, file_parent):
    if not isinstance(value, dict):
        new_dict = make_entry(key, value, level, '', file_parent)
    else:
        new_dict = make_entry(key, '', level,
                              make_list_entry(value, file_parent, level + 1),
                              file_parent)
    return new_dict


def merge_data(file1, file2, level=0):
    new_list = []
    for key, value in file1.items():
        if key not in file2:
            new_list.append(make_complex_entry(key, value, level, 'file1'))
        elif key in file2 and file2[key] == value:
            new_list.append(make_complex_entry(key, value, level, 'both'))
            file2.pop(key)
        elif key in file2 and file2[key] != value:
            if isinstance(value, dict) and isinstance(file2[key], dict):
                new_list.append(make_entry
                                (key, '', level, merge_data
                                    (value, file2[key], level + 1), 'both'))
            else:
                new_list.append(make_complex_entry
                                (key, value, level, 'file1'))
                new_list.append(make_complex_entry
                                (key, file2[key], level, 'file2'))
            file2.pop(key)
    new_list.extend(make_list_entry(file2, 'file2', level))
    return new_list


def make_diff_data(content1, content2):
    merged_data = merge_data(content1, content2)
    return merged_data
