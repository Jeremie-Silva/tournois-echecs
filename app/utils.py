import json


def file_opener(file) -> dict:
    with open(f"Data/{str(file)}.json", "r") as json_file:
        data = json.load(json_file)
    return data


def file_writer(file, data):
    with open(f"Data/{str(file)}.json", "w") as json_file:
        json.dump(data, json_file)


def object_to_dict(obj):
    if isinstance(obj, list):
        return [object_to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        return {key: object_to_dict(value) for key, value in obj.__dict__.items()}
    else:
        return obj
