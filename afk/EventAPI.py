import KeyOperator
from time import sleep # noqa
from threading import Thread # noqa
import os
import yysOS
import json
import yysKB
import re

command_key = False
userStatus = 0
inputList = []


def InitProc() -> None:
    global userStatus
    userStatus = 0
    folderPath = getUserAppPath()
    jsonPath = getJsonPath()
    userStatus = 1 if chkFileExist(folderPath) else (os.mkdir(folderPath))
    if userStatus == None: return # noqa
    userStatus = 2 if chkFileExist(jsonPath) else 1


def chkFileExist(path):
    return True if os.path.exists(path) else False


def writeInput():
    global inputList
    print("go to write!!!")
    if len(inputList) == 3:
        if inputList[0] == "" and inputList[1] == "" and inputList[2] == "":
            return
        else:
            data = {}
            data["WinName"] = yysOS.Title if inputList[0] == "" else inputList[0]
            data["interval"] = 3 if inputList[1] == "" else inputList[1]
            data["uCmdList"] = [yysOS.N1, yysOS.N7] if inputList[2] == "" else inputList[2]
            writeJson(jsonPath=getJsonPath(), date=data)


def provingDecimal(str1) -> bool:
    regex = yysOS.PatternPosNum
    mathc_obj = re.match(regex, str1)
    res = False
    if mathc_obj:
        res = True
    else:
        res = False
    return res


def writeJson(jsonPath: str, date: map) -> None:
    json_str = json.dumps(date)
    with open(jsonPath, 'w') as f:
        f.write(json_str)
        f.close()


def readJson(jsonPath: str) -> map:
    with open(jsonPath, 'r') as f:
        date = json.load(f)
        f.close()
    return date


def getUserAppPath() -> str:
    folderName = "!SjyTestfolder"
    adds = os.path.join(os.environ["APPDATA"], "..", "Local", "Packages")
    print(adds + '\\' + folderName)
    return (adds + '\\' + folderName)


def getJsonPath() -> str:
    jsonFName = 'thsss.json'
    folderPath = getUserAppPath()
    return folderPath + '\\' + jsonFName


def getAllInput(str1, str2, str3) -> None:
    global inputList
    inputList = []
    inputList.append(str1)
    inputList.append(str2)
    inputList.append(str3)


def EditParam() -> map:
    res = {
        "WinName": yysOS.Title,
        "interval": 3,
        "uCmdList": [yysOS.N1, yysOS.N7],
    }
    return res


def scheme2():
    global command_key
    command_key = False if command_key else True
    sleep(0.5)
    if command_key:
        thd = None
        thd = Thread(target=scheme2Task)  # 线程定义
        thd.start()  # 开启线程
        print("我按下了：" + str(command_key))
    else:
        thd = None
        print("我按下了：" + str(command_key))
        print("脚本关闭！")


def scheme2Task():
    print("脚本启动！")
    InitProc()
    ParamDate = getScriptParam()
    winList = yysKB.getPidForName(ParamDate["WinName"])
    i = 0
    while command_key:
        i += 1
        KeyOperator.btn1Task(interval=ParamDate["interval"], uCmdList=ParamDate["uCmdList"], WinNameList=winList)


def getScriptParam() -> map:
    global userStatus
    res = {}
    print('userStatus:' + str(userStatus))
    if userStatus == 2:
        res = EditParam()
    else:
        DefualtParamDate = {
            "WinName": yysOS.Title,
            "interval": 3,
            "uCmdList": [yysOS.N1, yysOS.N7],
        }
        res = DefualtParamDate
        writeInput()
    return res


if __name__ == '__main__':
    # InitProc()
    provingDecimal("111.0")
    pass
