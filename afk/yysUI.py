import tkinter as tk
from yysOS import * # noqa
import EventAPI


class YYSUI:
    def __init__(self) -> None:
        self.Win  = tk.Tk() # noqa
        self.Win.title(Win_Title) # noqa
        self.Win.geometry(Win_Size) # noqa
        # EventAPI.InitProc()

        # 主屏
        self.MainScreen = tk.Label(self.Win, text=MainScreen_OutputStr, bg=MainScreen_bg, # noqa
            width=MainScreen_width, height=MainScreen_height, # noqa
            padx=MainScreen_padx, pady=MainScreen_pady, borderwidth=MainScreen_borderwidth, # noqa
            relief=MainScreen_relief) # noqa

        # Interface
        self.lb1 = tk.Label(self.Win, text=lb1_text) # noqa
        self.input1 = tk.Entry(self.Win, width=input1_width) # noqa
        self.lb2 = tk.Label(self.Win, text=lb2_text) # noqa
        self.input2 = tk.Entry(self.Win, text="", width=input2_width) # noqa
        self.lb3 = tk.Label(self.Win, text=lb3_text) # noqa
        self.input3 = tk.Entry(self.Win, width=input3_width) # noqa

        # 按钮
        self.button1 = tk.Button(self.Win, text=button1_text, width=button1_width, command=self.btn1Action)  # noqa

        # 布局
        self.MainScreen.grid(row=0, columnspan=2)
        self.lb1.grid(row=1, column=0, sticky="E")
        self.input1.grid(row=1, column=1, sticky="w")
        self.lb2.grid(row=2, column=0, sticky="E")
        self.input2.grid(row=2, column=1, sticky="w")
        self.lb3.grid(row=3, column=0, sticky="E")
        self.input3.grid(row=3, column=1, sticky="w")
        self.button1.grid(row=4, columnspan=2)

        self.Win.resizable(False, False)  # 禁止改变窗口大小
        self.Win.mainloop()

    def getInput1(self):
        return self.input1.get()

    def getInput2(self):
        return self.input2.get()

    def getInput3(self):
        return self.input3.get()

    def btn1Action(self):
        print(self.getInput1() + self.getInput2() + self.getInput3())
        EventAPI.getAllInput(self.getInput1(), self.getInput2(), self.getInput3())
        EventAPI.scheme2()


if __name__ == '__main__':
    YYSUI()
