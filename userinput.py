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
