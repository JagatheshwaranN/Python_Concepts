# None means nothing i.e., no values associated. None is also an object.

def f1():
    return 10


x = f1()
print(x)


def f2():
    print('Hello')


y = f2()
print(y)

a = None
print(id(a))
print(type(a))

b = None
print(id(a))
print(type(a))


def f3():
    pass


c = f3()
print(id(c))
print(type(c))
