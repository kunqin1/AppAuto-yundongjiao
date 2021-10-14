import yaml

base_path = "../config/"


def read_yaml(fileName, key):
    if fileName is None:
        filePath = base_path
    else:
        filePath = base_path + fileName
    with open(filePath, encoding="UTF-8") as f:
        f1 = yaml.load(f)
        data = f1.get(key)
        return data
        # print(data)
        # print(data["rank"]["name"])
