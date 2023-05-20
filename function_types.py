# In python, a function is a block of code which only runs when it called.
# Function can accept arguments and also return values.
# It is created using def keyword.

# Create & Call Function.
# Function Parameters / Arguments.
# Function Arbitrary Arguments.
# Function Keyword Arguments.
# Function Arbitrary Keyword Arguments.
# Default Parameter Value.
# Pass Any Data Types as an Argument to a Function.
# Function with Return Value.
# Function with Pass Statement.

def simple_func():
    print("Hello, I'm Python Function")


simple_func()


def func_wt_args(name, age):
    print("Hello {}, you are {} years old".format(name, age))


func_wt_args('John', 29)


def func_wt_arb_args(*fruits):
    for fruit in fruits:
        print(fruit)


func_wt_arb_args('apple', 'orange', 'mango', 'grapes')


def func_wt_keyword_args(name, age):
    message = "Hello {}, you are {} years old".format(name, age)
    print(message)


func_wt_keyword_args(name='John', age='29')
func_wt_keyword_args(age='27', name='Alex')


def func_wt_abr_key_args(**dataset):
    for data in dataset:
        print(data, dataset[data])


func_wt_abr_key_args(name='John', age='29', city='New York')
