import time
import yysKB


def SingleMode(uCmdList: int, WinNameList: list):
    # yysKB.peassKey(yysOS.N1, yysOS.N7)
    for uCmd in uCmdList:
        yysKB.peassOneKey(uCmd=uCmd, resList=WinNameList)


def btn1Task(interval: int, uCmdList: list, WinNameList: list):
    SingleMode(uCmdList=uCmdList, WinNameList=WinNameList)
    print("dododo:" + "执行中...")
    time.sleep(interval)
