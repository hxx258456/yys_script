from threading import Thread,Lock
 
 
global_num = 0
 
def func1():
	global global_num
	for i in range(1000000):
		lock.acquire()#两个线程会最开始抢这个锁，拿到锁就会处于关锁，执行后面的程序，其他线程执行处于监听状态，等待这个线程开锁，再抢锁
		global_num += 1
		lock.release()
	print('---------func1:global_num=%s--------'%global_num)
 
def func2():
	global global_num
	for i in range(1000000):
		lock.acquire()
		global_num += 1
		lock.release()
	print('--------fun2:global_num=%s'%global_num)
print('global_num=%s'%global_num)
 
lock = Lock()
 
t1 = Thread(target=func1)
t1.start()
 
t2 = Thread(target=func2)
t2.start()