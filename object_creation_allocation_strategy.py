# All fundamental data types of Python are immutable.
# Once we create an object, we can’t perform any changes in the object.
# If we are trying to perform any changes, then with those changes a new object will be created.
# Everything in PYTHON is OBJECT
# In Python, if object is need to be created the PVM won’t create it blindly.
# First it will check whether any object is already created and holding the value.
# If it’s there, then PVM reuse the same object otherwise will create new object.

x = 10
print(x)
print(id(x))  # 2919709567568

x = x+1
print(x)
print(id(x))  # 2919709567600

y = 10
z = y
print(y)
print(id(y))  # 2919709567568
print(z)
print(id(z))  # 2919709567568
z = y+1
print(z)
print(id(z))  # 2919709567600

a = 10
b = 10
c = 10
print(a)
print(b)
print(c)
print(id(a))  # 2919709567568
print(id(b))  # 2919709567568
print(id(c))  # 2919709567568
