# try with except
# a = 10
try:
    print(a)
except NameError as ne:
    print(ne)

print("====================================")

# try with multiple excepts
a = 10
try:
    print(a)
    print(a / 0)
except NameError as ne:
    print(ne)
except ArithmeticError as ae:
    print(ae)

print("====================================")

# try with except and else
# b = 20
try:
    print(b)
except NameError as ne:
    print('Something went wrong')
    print(ne)
else:
    print('Nothing wrong, program executed')

print("====================================")

# try with except and finally
try:
    f = open("demo.txt")
    f.write("Learning Python")
except FileNotFoundError as e:
    print(e)
finally:
    print('Closing the file')

print("====================================")

# Raise Exception
number = input("Enter any number")
number = int(number)
if not type(number) is int:
    raise TypeError("Only integer type data is allowed")

print("====================================")

# To get the list of builtin errors and exceptions in Python

for exception in dir(locals()['__builtins__']):
    print(exception)

print("====================================")


class AgeValidateError(Exception):

    def __init__(self, msg):
        self.msg = msg


age = int(input("Enter your age to verify whether your eligible to vote \n"))
if age < 18:
    raise AgeValidateError("Age is less than 18")
else:
    print('You are eligible to vote')

print("====================================")

try:
    print("Try block")
except ArithmeticError:
    print("Except block")
else:
    print("Else block")
finally:
    print("Finally block")

print("====================================")

try:
    print("Try block")
    print(10/0)
except ArithmeticError:
    print("Except block")
else:
    print("Else block")
finally:
    print("Finally block")
