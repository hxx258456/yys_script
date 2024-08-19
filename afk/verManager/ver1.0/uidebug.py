from time import sleep
import tkinter as tk
from yysOS import * # noqa
from threading import Thread
import threading

# 创建条件变量
condition_var = threading.Condition()
command_key = 0
# mutex_lock = threading.Lock()
# 创建事件
stop_event = threading.Event()

'''
def testb():
    global command_key
    command_key = 0 if command_key == 1 else 1
    with condition_var:
        condition_var.notify()
    print("我按下了：" + str(command_key))
    return
'''


def testb2():
    global command_key
    command_key = 0 if command_key == 1 else 1
    print("按下了" + str(command_key))
    if command_key == 1:
        thd = Thread(target=get_command2)  # 线程定义
        thd.start()  # 开启线程
        # stop_event.clear()
        stop_event.set()
        print("开启线程:" + str(command_key))
    else:
        stop_event.clear()
        print("close线程:" + str(command_key))
        # stop_event.set()
    return


def get_command2():
    global command_key
    i = 0
    while stop_event.is_set():
        # if command_key != 1: break
        print("cmd线程收到的值：" + str(command_key))
        sleep(1)
        i += 1
        MainScreen.config(text=i, bg='#bfe87d')
    print("退出ok")

'''
def get_command():
    global command_key

    while True:
        with condition_var:
            condition_var.wait()
            # sleep(1)
            print("cmd线程收到的值：" + str(command_key))
            i = 0
            while command_key == 1:
                if command_key != 1: break
                sleep(1)
                i += 1
                MainScreen.config(text=i, bg='#bfe87d')
'''


Win  = tk.Tk() # noqa
Win.title(Win_Title) # noqa
Win.geometry(Win_Size) # noqa

OutputStr = "nmsl"
MainScreen = tk.Label(Win, text=OutputStr, bg=MainScreen_bg, # noqa
    width=MainScreen_width, height=MainScreen_height, # noqa
    padx=MainScreen_padx, pady=MainScreen_pady, borderwidth=MainScreen_borderwidth, # noqa
    relief=MainScreen_relief) # noqa

button1 = tk.Button(Win, text='开关', width=7, command=testb2)
# button2 = tk.Button(Win, text='开关', command=testb)

lbk = tk.Label(Win)

lb1 = tk.Label(Win, text='窗     口      名      称 ：')
input1 = tk.Entry(Win, width=20)
lb2 = tk.Label(Win, text='按  键  间  隔  （秒） ：')
input2 = tk.Entry(Win, width=5)
lb3 = tk.Label(Win, text='指定按键（单轮模式）：')
input3 = tk.Entry(Win, width=10)

MainScreen.grid(row=0, columnspan=2)
lb1.grid(row=1, column=0, sticky="E")
input1.grid(row=1, column=1, sticky="w")
lb2.grid(row=2, column=0, sticky="E")
input2.grid(row=2, column=1, sticky="w")
lb3.grid(row=3, column=0, sticky="E")
input3.grid(row=3, column=1, sticky="w")
button1.grid(row=4, columnspan=2)

# thd = Thread(target=get_command2)  # 线程定义
# thd.start()  # 开启线程

'''
MainScreen.pack(fill="x")

# button1.pack(side="left", anchor="nw")
lb1.pack(side="left", anchor="nw")
input1.pack(side="left", anchor="nw")
button2.pack(side="right", anchor="ne")

lbk.pack(side="left", fill="x")

lb2.pack(side="left", anchor="nw")
input2.pack(side="left", anchor="nw")
'''

Win.resizable(False, False)
Win.mainloop()
