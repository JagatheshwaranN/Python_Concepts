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


# filter() - Filter function can be used to filter the values from the
# set of data / sequence based on some condition.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


lst = [0, 5, 10, 15, 20, 25, 30]
lst_1 = list(filter(is_even, lst))
print(lst_1)

lst_2 = list(filter(lambda x: x % 2 == 0, lst))
print(lst_2)

lst_3 = list(filter(lambda x: x % 2 != 0, lst))
print(lst_3)

# map() - Map function can be used to perform the manipulation on the set of
# data / sequence based on some condition.


def double_value(x):
    return x * 2


lst2 = [1, 2, 3, 4, 5]
lst_4 = list(map(double_value, lst2))
print(lst_4)

lst_5 = list(map(lambda x: x * 2, lst2))
print(lst_5)

lst3 = [1, 2, 3, 4, 5]
lst4 = [10, 20, 30, 40, 50]
lst_6 = list(map(lambda x, y: x * y, lst3, lst4))
print(lst_6)
