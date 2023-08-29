import threading
from threading import *

print(threading.current_thread().getName())


# Create Thread without using any class
def display():
    print("The display function is executed by Thread :", current_thread().getName() + "\n")


thread = Thread(target=display)
thread.start()
print("This code is executed by Thread :", current_thread().getName() + "\n")


# Create Thread by extending the thread class
class MyThread(Thread):
    def run(self):
        for j in range(10):
            print("Child Thread")


t = MyThread()
t.start()
for i in range(10):
    print("Main Thread")


# Create thread without extending the thread class
class MyThread1:
    def show(self):
        for j in range(10):
            print("Child Thread2 : ", current_thread().getName()+"\n")


obj = MyThread1()
t2 = Thread(target=obj.show)
t2.start()
for i in range(10):
    print("Main Thread2 : ", current_thread().getName() + "\n")
