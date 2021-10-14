import json

base_path = "../config/"


def read_json(file_name, key=None):
    if file_name is None:
        file_path = base_path
    else:
        file_path = base_path + file_name
    with open(file_path, encoding='UTF-8') as f:
        f = json.load(f)
        if key is None:
            return None
        else:
            # 通过key来获取每个定位所有信息
            data = f.get(key)
            return data


def get_value(key, file_path, key1):
    data = read_json(file_path, key1)
    # print(data.get(key))
    return data.get(key)


if __name__ == '__main__':
    # read_json("rank.json", "EnterRank")
    get_value("type", "rank.json", "EnterRank")

