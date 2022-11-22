import yaml
import json
from os.path import splitext


def read_file(file_path):
    file_ext = splitext(file_path)[1]
    with open(file_path, 'r') as data:
        output = data.read()
        if file_ext == '.json':
            return output, 'json'
        elif file_ext == '.yaml' or file_ext == '.yml':
            return output, 'yml'
        else:
            print(file_ext)
            raise Exception('This file type is not supported')


def parse_data(data, data_format):
    output = {}
    if data:
        if data_format == 'yml':
            output = yaml.safe_load(data)
        elif data_format == 'json' and data:
            output = json.loads(data)
    return output


def get_data(file_path):
    data, data_format = (read_file(file_path))
    output = parse_data(data, data_format)
    return output
