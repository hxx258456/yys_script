import threading
from time import sleep


# 定义全局变量
global_var = 0
# 定义条件变量
cond = threading.Condition()
# 子线程函数
def child_thread():
    global global_var
    while True:
    # 获取条件变量
        with cond:
            # 等待条件变量
            cond.wait()
            while global_var == 1:
                # 条件满足后执行操作
                print('global_var changed:', global_var)
                sleep(1)
            print('global_var changed:', global_var)

# 创建子线程
t = threading.Thread(target=child_thread)
t.start()
# 主线程修改全局变量
global_var = 1
# 通知条件变量
with cond:
    cond.notify()
    
sleep(3)

global_var = 2
# 通知条件变量
with cond:
    cond.notify()
    
sleep(3)

global_var = 1
# 通知条件变量
with cond:
    cond.notify()