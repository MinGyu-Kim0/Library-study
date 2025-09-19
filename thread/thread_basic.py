import threading
import time

def printA():
    for i in range(1, 11, 2):
        print(i)
        time.sleep(0.1)


def printB():
    for i in range(2, 11, 2):
        print(i)
        time.sleep(0.1)

t1 = threading.Thread(target=printA)
t2 = threading.Thread(target=printB)

t1.start()
t2.start()
