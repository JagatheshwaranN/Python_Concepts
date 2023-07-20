# In python 3, we have input function which is used to get the value from the user as string data type.

name = input("Enter your name : ")
age = input("Enter your age : ")

# We can use {} symbol for interpolation. Interpolation means substitute a value.
# We can do this by using format function.
print("Hello {}, you are {} years old".format(name, age))

print(type(name))
print(type(age))

# To convert age from String to Int
age = int(age)
print(type(age))

# To read multiple values in single line
a, b = [int(x) for x in input("Enter 2 numbers").split()]
print("a :", a)
print("b :", b)
print("Sum :", a + b)

c, d = [float(x) for x in input("Enter 2 numbers").split(',')]
print("c :", c)
print("d :", d)
print("Sum :", c + d)

# Eval - This function is going to take the expression as input and print the result.
# It is used to convert the given data / input into the internal type automatically.

expression = input("Enter the expression")
result = eval(expression)
print(result)

input_data = eval(input("Enter the value"))
print(type(input_data))

# Eval function is used to take multiple values of different data types.

e, f, g = [eval(x) for x in input("Enter 3 values").split(',')]
print("e :", e)
print("f :", f)
print("g :", g)
