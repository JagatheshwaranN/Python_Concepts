# x = Lambda arguments : expression

def cube(n):
    return n * n * n


cube = cube(3)
print(cube)

cube_of_number = lambda num: num * num * num
print(cube_of_number(5))


def my_fun(n):
    return lambda a: a * n


my_doubler = my_fun(2)
print(my_doubler(10))
print(my_doubler(20))
