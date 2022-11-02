import yaml


def get_data(file_path):
    with open(file_path, 'r') as file:
        if '.yaml' in file_path or '.yml' in file_path:
            data = yaml.load(file, Loader=yaml.FullLoader)
            if not data:
                return []
            list_from_yaml = [f'{str(x)}: {str(y)}'.lower()
                              for x, y in data.items()]
            return list_from_yaml
        elif '.json' in file_path:
            list_from_json = []
            for index in file:
                list_from_json.append(index.strip().lower().replace('\"', '')
                                      .replace("\'", '').replace(",", ''))
            return list_from_json[1:-1]
