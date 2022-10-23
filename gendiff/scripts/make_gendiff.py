def make_dict_from_json(file):
    with open(file, 'r') as file:
        dict_from_json = []
        for index in file:
            dict_from_json.append('  ' + index.strip().replace('\"', '').replace("\'", '').replace(",", ''))
    return dict_from_json[1:-1]


def get_key(string):
    return string[:string.find(':')]


def get_value(string):
    return string[string.find(':') + 1:]


def change_third_sigh(list, sign):
    new_string = ''
    for string in list:
        new_string = new_string + '  ' + (sign + string[1:]) + '\n'
    return new_string


def generate_diff(file_1, file_2):
    first_dict = make_dict_from_json(file_1)
    second_dict = make_dict_from_json(file_2)
    first_dict.sort(key=lambda x: x.lower())
    second_dict.sort(key=lambda x: x.lower())
    first_index = 0
    second_index = 0
    output = '{\n'
    while first_index != len(first_dict) or second_index != len(second_dict):
        if first_index == len(first_dict):
            rest_of_list = change_third_sigh(second_dict[second_index:], '+')
            output += rest_of_list
            break
        elif second_index == len(second_dict):
            rest_of_list = change_third_sigh(first_dict[first_index:], '-')
            output += rest_of_list
            break
        if first_dict[first_index] == second_dict[second_index]:
            output += ('  ' + first_dict[first_index] + '\n')
            first_index += 1
            second_index += 1
        elif get_key(first_dict[first_index]) != get_key(second_dict[second_index]):
            temp_dict = [first_dict[first_index].lower(), second_dict[second_index].lower()]
            temp_dict.sort()
            if temp_dict[0] == first_dict[first_index].lower():
                output += ('  ' + (first_dict[first_index].replace('  ', '- ')) + '\n')
                first_index += 1
            else:
                output += ('  ' + (second_dict[second_index].replace('  ', '+ ')) + '\n')
                second_index += 1
        else:
            output += ('  ' + ('- ' + first_dict[first_index]) + '\n')
            first_index += 1
            output += ('  ' + ('+ ' + second_dict[second_index]) + '\n')
            second_index += 1
    output += '}'
    return output

