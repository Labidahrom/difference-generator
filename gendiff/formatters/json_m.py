import json


def render_to_json(data):
    return json.dumps(data, indent=2)
