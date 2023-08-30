import time
from threading import *


def double(nums):
    for n in nums:
        time.sleep(1)
        print('Double of {} : '.format(n), n * 2)
        print()


def square(nums):
    for n in nums:
        time.sleep(1)
        print('Square of {} : '.format(n), n * n)
        print()


numbers = [1, 2, 3, 4, 5]
begin_time = time.time()
thread1 = Thread(target=double, args=(numbers,))
thread2 = Thread(target=square, args=(numbers,))

print(thread1.getName())
thread1.setName('John')
print(thread1.getName())
print()

print(thread2.getName())
thread2.setName('Alex')
print(thread2.getName())
print()

thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time.time()
print("The total time taken : ", end_time - begin_time)
