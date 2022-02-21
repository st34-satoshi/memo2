import json


def save_json(file_name):
    json_data = {"name": "taka"}
    with open(file_name, mode="w") as f:
        json.dump(json_data, f)


def read_json(file_name):
    with open(file_name, mode="r") as f:
        json_data = json.load(f)
        print(json_data)


if __name__ == '__main__':
    file_path = "test.json"
    # save_json(file_path)
    read_json(file_path)