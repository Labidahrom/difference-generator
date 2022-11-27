def make_entry(key, action, value, children):
    new_dict = {
        'key': key,
        'value': value,
        'action': action,
        'children': children
    }
    return new_dict


def merge_data(content1, content2):
    output = []
    removed = content1.keys() - content2.keys()
    added = content2.keys() - content1.keys()
    same = sorted(content1.keys() | content2.keys())
    for key in same:
        if key in removed:
            output.append(make_entry(key, 'removed', content1[key], ''))
        elif key in added:
            output.append(make_entry(key, 'added', content2[key], ''))
        elif content1[key] == content2[key]:
            output.append(make_entry(key, 'same', content1[key], ''))
        else:
            if isinstance(content1[key], dict) and \
                    isinstance(content2[key], dict):
                output.append(make_entry
                              (key, 'nested', '',
                               merge_data(content1[key], content2[key])))
            else:
                output.append(make_entry(key, 'removed', content1[key], ''))
                output.append(make_entry(key, 'added', content2[key], ''))
    return output


def make_diff_data(content1, content2):
    merged_data = merge_data(content1, content2)
    return merged_data
