import json


def make_json_data(data):
    output = json.dumps(data, indent=2)
    return output
