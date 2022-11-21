import yaml
import json


def read_file(file_path):
    with open(file_path, 'r') as data:
        output = data.read()
        if '.json' in file_path:
            return output, 'json'
        elif '.yaml' in file_path or '.yml' in file_path:
            return output, 'yml'


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
