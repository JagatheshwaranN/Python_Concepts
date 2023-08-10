# In python, a function is a block of code which only runs when it called.
# Function can accept arguments and also return values.
# It is created using def keyword.


# Create & Call Function.
def simple_func():
    print("Hello, I'm Python Function")


simple_func()


# Function Parameters / Arguments.
def func_wt_args(name, age):
    print("Hello {}, you are {} years old".format(name, age))


func_wt_args('John', 29)


# Function Arbitrary Arguments.
# *args - It is known as variable length argument in Python. It is used to take more than one value or no value at all.
# *args - It should be the last argument to the method.
def func_wt_arb_args(*fruits):
    for fruit in fruits:
        print(fruit)


func_wt_arb_args('apple', 'orange', 'mango', 'grapes')


# Function Keyword Arguments.
def func_wt_keyword_args(name, age):
    message = "Hello {}, you are {} years old".format(name, age)
    print(message)


func_wt_keyword_args(name='John', age='29')
func_wt_keyword_args(age='27', name='Alex')


# Function Arbitrary Keyword Arguments.
# **kwargs - It is known as variable length keyword argument in Python. It is used to take more than one value
# or no value at all. This argument holds key value pairs.
# **kwargs - It should be the last argument to the method.
def func_wt_abr_key_args(**dataset):
    for data in dataset:
        print(data, dataset[data])


func_wt_abr_key_args(name='John', age='29', city='New York')


# Default Parameter Value.
def func_wt_default_param(name, age, city='Seattle'):
    message = "Hello {}, you are {} years old and living in {}".format(name, age, city)
    print(message)


func_wt_default_param('John', 29)


# Pass Any Data Types as an Argument to a Function.
def func_any_datatype_passed(fruits):
    for fruit in fruits:
        print(fruit)


func_any_datatype_passed(['apple', 'orange', 'mango', 'grapes'])


# Function with Return Value.
def func_wt_return_val(name, age, city='Seattle'):
    return "Hello {}, you are {} years old and living in {}".format(name, age, city)


print(func_wt_return_val('John', 29))


# Function with Pass Statement.
def func_wt_no_content():
    pass


# Nested Functions
def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    print("Outer Function return Inner Function")
    return inner


f1 = outer()  # It's a function call
f1()
f2 = outer  # Here, For outer function we are giving another name


# Function Decorator

def decorator(func):
    def inner(name):
        if name == 'Alex':
            print("Hello", name, "Good Evening")
        else:
            func(name)

    return inner


@decorator
def wish(name):
    print("Hello", name, "Good Morning")


wish('John')
wish('Alex')
