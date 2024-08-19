from MainDemo import yysOperator
from time import sleep
from threading import Thread # noqa


# 创建条件变量
condition_var = None
command_key = False


def TaskInit(a1, b2):
    global condition_var
    global command_key
    condition_var = a1
    command_key = b2


def changeOnOff():
    global command_key
    command_key = False if command_key else True
    with condition_var:
        condition_var.notify()
    print("我按下了：" + str(command_key))


def get_command():
    global command_key
    while True:
        with condition_var:
            i = 0
            while command_key:
                sleep(1)
                i += 1
                print("dododo" + str(i))
                yysOperator.testdebug(i)
                sleep(1)
        sleep(1)
        print("外层等待")

# plan two_Start


def EditParam(str1, str2, str3) -> None:
    print("EditParam")


def scheme2():
    global command_key
    command_key = False if command_key else True
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
    i = 0
    while command_key:
        i += 1
        yysOperator.testdebug(i)
# plan two_End
