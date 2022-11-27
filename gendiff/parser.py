import yaml
import json
from os.path import splitext


def read_file(file_path):
    _, file_ext = splitext(file_path)
    with open(file_path, 'r') as data:
        output = data.read()
        return output, file_ext[1:]


def parse_data(data, data_format):
    output = {}
    if data:
        if data_format == 'yml' or data_format == 'yaml':
            output = yaml.safe_load(data)
        elif data_format == 'json':
            output = json.loads(data)
        else:
            raise Exception('This file type is not supported')
    return output


def get_data(file_path):
    data, data_format = (read_file(file_path))
    output = parse_data(data, data_format)
    return output
