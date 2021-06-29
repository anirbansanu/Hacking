from threading import *
import time


def file_write(string):
    s = time.time()
    f = open("sample.py", "w")
    f.write(string)
    f.close()
    e=time.time()
    print("done in : ", e - s)


def f2(str):
    for x in str:
        time.sleep(1)
        print(x)


s = time.time()
"""t1 = Thread(target=f1, args=("this is",))

t2 = Thread(target=f2, args=("2 ,2 , 2",))
t1.start()
t2.start()
t1.join()
t2.join()"""
#f1("this is")
#f2("2 ,2 , 2")
e = time.time()
print("done in : ", e-s)

