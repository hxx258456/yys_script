# from threading import Thread
from yysUI import YYSUI # noqa
import EventAPI # noqa
import threading # noqa
import os
import json


def testd():
    folderName = "!SjyTestfolder"
    jsonFName = 'thsss.json'
    adds = os.path.join(os.environ["APPDATA"], "..", "Local", "Packages")
    folderPath = adds + '\\' + folderName
    jsonPath = folderPath + '\\' + jsonFName
    print("文件夹存在" if os.path.exists(folderPath) else (os.mkdir(folderPath)))
    # print(adds)
    print(folderPath)
    # print("存在" if os.path.exists(folderPath) else "不存在")
    date = {
        "name": "json"
    }

    # write
    json_str = json.dumps(date)
    with open(jsonPath, 'w') as f:
        f.write(json_str)

    # read
    with open(jsonPath, 'r') as f:
        date2 = json.load(f)
        print(date2["name"])

    # delete
    print((os.remove(jsonPath)) if os.path.exists(jsonPath) else "不存在")


if __name__ == '__main__':
    YYSUI()
