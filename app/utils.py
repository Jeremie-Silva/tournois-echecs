import json
from typing import Union, Any


def file_opener(file: str) -> dict:
    """The function needs a file name, opens the file in question in read-only mode,
    extracts all the data in json format and returns a dict containing all the data"""
    with open(f"Data/{str(file)}.json", "r") as json_file:
        data: dict = json.load(json_file)
    return data


def file_writer(file: str, data: dict) -> None:
    """The function needs a file name and a dict, opens the file in question in write mode,
    overwrites all the data in the file with the dict converted to json format"""
    with open(f"Data/{str(file)}.json", "w") as json_file:
        json.dump(data, json_file)


def object_to_dict(obj: object) -> Union[list, dict, Any]:
    """It is a recursive function that needs an object, goes through this object
    and converts each of the objects contained in it into a list or dictionary.
    For example if the object has a list of Players then a list of values will be returned"""
    if isinstance(obj, list):
        return [object_to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        return {key: object_to_dict(value) for key, value in obj.__dict__.items()}
    else:
        return obj
