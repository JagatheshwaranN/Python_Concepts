# A name in python program is called as Identifiers. It can be variable name, method name or class name.
# a = 10
# class Test:

# Rules to define Python Identifiers
# 1.	Allowed chars for Python identifiers are a-z, A-Z, 0-9, & _.
# 2.	Identifiers can’t start with digits. If it has taken, then syntax error will be thrown.
# 3.	Python Identifiers are case sensitive. (total=20, Total=30, TOTAL=40 is different and not same).
# 4.	No length limit for identifiers but not recommended to take lengthy identifier.
# 5.	We can’t take keyword/reserved word as identifier.

# Note on variables
# X -> Normal Variable
# _X -> Protected Variable
# __X -> Private Variable
# __X__ -> Magic Variable

# Python Variables
age = 18
dateOfBirth = "January"
_city = "Chennai"

# Scope - Global and Local Variables
# 1.	A variable declared inside the function is called as Local variable.
# 2.    A variable declared  at the outside of any function is called as Global variable.
# 3.	We can use the Global variable inside the function.
# 4.    If needed we can update the Global variable value inside the function.

var = 100  # Global variable


def out_function():
    # global var
    # When we use Global var inside function.
    # Then its value will be updated as per var value inside the function
    var = 50  # Local variable
    print(var)  # 50 - Local var


out_function()
print(var)  # 100 - Global var

# Variable Assignment
name, city = 'John', 'Seattle'
print(name)
print(city)

city1 = city2 = city3 = 'Los Angeles'
print(city1)
print(city2)
print(city3)

icecream = ['vanilla', 'strawberry', 'mango', 'chocolate']
a, b, c, d = icecream
print(a)
print(b)
print(c)
print(d)
