import multiprocessing
import threading as th
import time

print(multiprocessing.current_process())
print(th.current_thread())


def fun1():
    while True:
        print('子进程正在执行')
        time.sleep(5)


def fun2():
    while True:
        print('线程正在执行')
        time.sleep(2)


if __name__ == '__main__':
    # 多进程
    process1 = multiprocessing.Process(target=fun1, name='鱼的小弟', daemon=True)     # 进程, daemon：守护模式，主进程不等待子进程
    process1.is_alive()     # 进程状态F
    process1.start()
    print('当前处于那个进程:', multiprocessing.current_process())  # 获取当前进程对象
    print('进程名', process1.name)
    print(process1.pid)  # 进程PID
    process1.is_alive()     # 进程状态T
    # process1.join()     # 进程暂停，等待子进程运行完毕才继续
    time.sleep(2)
    print('主进程结束')
    # process1.terminate()        # 进程终止，线程无法终止，只能等待其结束
    print('主进程结束')

    # 多线程
    # threading1 = th.Thread(target=fun2, name='鱼的小弟')                 # 线程
    # threading1.start()
    # print(threading1.ident)  # 线程ident
    # print('线程名：', threading1.name)
    # print('当前处于哪个线程:', th.current_thread())
