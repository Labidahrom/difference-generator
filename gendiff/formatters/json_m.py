import json


def render_to_json(data):
    output = json.dumps(data, indent=2)
    return output
