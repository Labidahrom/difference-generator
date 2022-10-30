def make_list_from_json(file):
    with open(file, 'r') as file:
        list_from_json = []
        for index in file:
            list_from_json.append(index.strip().replace('\"', '')
                                  .replace("\'", '').replace(",", ''))
    return list_from_json[1:-1]


def add_sign(item, sign, num=''):
    return f'  {sign} {item}\n'.replace(':', f':{num}')


def clear_num(item):
    return item.replace(':1', ':').replace(':2', ':')


def generate_diff(file_1, file_2):
    output_list = []
    output_string = '{\n'
    file_1_set = set(make_list_from_json(file_1))
    file_2_set = set(make_list_from_json(file_2))
    if not file_1_set and not file_2_set:
        return ''
    file_1_items = file_1_set - file_2_set
    file_2_items = file_2_set - file_1_set
    file_1_file_2_items = file_1_set & file_2_set
    output_list.extend([add_sign(item, '-', '1') for item in file_1_items])
    output_list.extend([add_sign(item, '+', '2') for item in file_2_items])
    output_list.extend([add_sign(item, ' ') for item in file_1_file_2_items])
    output_list.sort(key=lambda x: x[4:].lower())
    output_list = list(map(clear_num, output_list))
    return output_string + ''.join(output_list) + '}'
