def make_entry(key, action, value, children, old_value='not_duplicated'):
    output = {
        'key': key,
        'action': action,
        'value': value,
        'children': children,
        'old_value': old_value,
    }
    if isinstance(value, dict) or isinstance(children, list):
        output['action'] += '-nested'
    return output


def build_diff(content1, content2):
    output = []
    removed = content1.keys() - content2.keys()
    added = content2.keys() - content1.keys()
    common_keys = sorted(content1.keys() | content2.keys())
    for key in common_keys:
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
                              (key, 'same', '',
                               build_diff(content1[key], content2[key])))
            else:
                output.append(make_entry(key, 'removed', content1[key],
                                         '', 'duplicated'))
                output.append(make_entry(key, 'added', content2[key],
                                         '', content1[key]))
    return output
