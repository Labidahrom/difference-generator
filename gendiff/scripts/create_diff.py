def make_item(item, file, level=0):
    new_list = []
    if not item:
        return new_list
    for i, j in item.items():
        if not isinstance(j, dict):
            new_dict = {
                'key': i,
                'value': j,
                'level': level,
                'children': '',
                'file': file
            }
        else:
            new_dict = {
                'key': i,
                'value': '',
                'level': level,
                'children': make_item(j, file, level + 1),
                'file': file
            }
        new_list.append(new_dict)
    return new_list


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


def check_key(key, list):
    for i in list:
        if i['key'] == key:
            return True
    return False


def get_item(key, list):
    for i in list:
        if i['key'] == key:
            return i


def get_index(item, given_list):
    return given_list.index(item)


def merge(data1, data2):
    for i in data2:
        if not check_key(i['key'], data1):
            i['file'] = 'file2'
            data1.append(i)
        else:
            if i['children'] and get_item(i['key'], data1)['children']:
                data1[get_index(get_item(i['key'], data1), data1)]['file']\
                    = 'both'
                merge(data1[get_index(get_item(i['key'], data1),
                                      data1)]['children'],
                      data2[get_index(i, data2)]['children']
                      )
            elif i['value'] != get_item(i['key'], data1)['value']:
                i['file'] = 'file2'
                data1.append(i)
            else:
                data1[get_index(get_item(i['key'], data1), data1)]['file']\
                    = 'both'
    return data1


def has_sighned_children(item):
    if item['children']:
        for i in item['children']:
            if i['file'] != 'both':
                return True
        return False


def make_children_unsigned(tree):
    for i in range(len(tree['children'])):
        tree['children'][i]['file'] = 'both'


def change_sign(tree):
    for i in tree:
        if has_sighned_children(i) and i['children']:
            change_sign(i['children'])
            if i['file'] != 'both' and has_sighned_children(i):
                make_children_unsigned(tree[get_index(i, tree)])


def make_diff_data(file1, file2):
    data1 = make_item(file1, 'file1')
    data2 = make_item(file2, 'file2')
    merged_data = merge(data1, data2)
    return merged_data
