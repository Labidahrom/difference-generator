import yaml
import json


def get_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        if '.yaml' in file_path or '.yml' in file_path:
            data = yaml.load(file, Loader=yaml.FullLoader)
        elif '.json' in file_path and file.read():
            data = json.load(open(file_path))
    return data
