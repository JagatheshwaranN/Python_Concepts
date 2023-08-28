import threading
from threading import *

print(threading.current_thread().getName())


def display():
    print("The display function is executed by Thread :", current_thread().getName()+"\n")


thread = Thread(target=display)
thread.start()
print("This code is executed by Thread :", current_thread().getName()+"\n")
