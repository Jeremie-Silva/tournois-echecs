import json


def file_opener(file) -> dict:
	with open(f"Data/{str(file)}.json", "r") as json_file:
		data = json.load(json_file)
	return data

def file_writer(file, data):
	with open(f"Data/{str(file)}.json", "w") as json_file:
		json.dump(data, json_file)