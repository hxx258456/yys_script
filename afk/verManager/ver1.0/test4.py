from time import sleep
import tkinter as tk
from yysOS import * # noqa
from threading import Thread
import threading
from MainDemo import yysOperator

# 创建条件变量
condition_var = threading.Condition()
command_key = False
# mutex_lock = threading.Lock()


def testb():
    global command_key
    command_key = False if command_key else True
    with condition_var:
        condition_var.notify()
    print("我按下了：" + str(command_key))
    pass


def get_command():
    global command_key
    while True:
        with condition_var:
            # sleep(1)
            # condition_var.wait()
            # print("cmd线程收到的值：" + str(command_key))
            i = 0
            # yysOperator.testdebug(tiptk=command_key)
            while command_key:
                sleep(1)
                i += 1
                print("dododo" + str(i))
                yysOperator.testdebug(i)
                # MainScreen.config(text=i, bg='#bfe87d')
                sleep(1)
        sleep(1)
        print("外层等待")


Win  = tk.Tk() # noqa
Win.title(Win_Title) # noqa
Win.geometry(Win_Size) # noqa

OutputStr = "nmsl"
MainScreen = tk.Label(Win, text=OutputStr, bg=MainScreen_bg, # noqa
    width=MainScreen_width, height=MainScreen_height, # noqa
    padx=MainScreen_padx, pady=MainScreen_pady, borderwidth=MainScreen_borderwidth, # noqa
    relief=MainScreen_relief) # noqa

button1 = tk.Button(Win, text='开关', width=7, command=testb)
button2 = tk.Button(Win, text='开关', command=testb)

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

thd = Thread(target=get_command)  # 线程定义
thd.start()  # 开启线程

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
