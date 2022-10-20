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


def generate_diff(file_1, file_2):
    first_dict = make_dict_from_json(file_1)
    second_dict = make_dict_from_json(file_2)
    first_dict.sort(key=lambda x: x.lower())
    second_dict.sort(key=lambda x: x.lower())
    first_index = 0
    second_index = 0
    output = []
    while first_index != len(first_dict) or second_index != len(second_dict):
        if first_index == len(first_dict):
            output.extend(second_dict[second_index:])
            break
        elif second_index == len(second_dict):
            output.extend(first_dict[first_index:])
            break
        if first_dict[first_index] == second_dict[second_index]:
            output.append(first_dict[first_index])
            first_index += 1
            second_index += 1
        elif get_key(first_dict[first_index]) != get_key(second_dict[second_index]):
            temp_dict = [first_dict[first_index].lower(), second_dict[second_index].lower()]
            temp_dict.sort()
            if temp_dict[0] == first_dict[first_index].lower():
                output.append(first_dict[first_index].replace('  ', '- '))
                first_index += 1
            else:
                output.append(second_dict[second_index].replace('  ', '+ '))
                second_index += 1
        else:
            output.append('- ' + first_dict[first_index])
            first_index += 1
            output.append('+ ' + second_dict[second_index])
            second_index += 1
    print('{')
    for i in output:
        print(' ', i)
    print('}')


if __name__ == '__main__':
    generate_diff(file_1, file_2)
