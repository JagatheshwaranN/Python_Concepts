# The Bool data type is used to perform the conditional check and return logical values (either True or False).
# In Python, we should use Capital T and F for True and False.

a = True
print(a)
print(type(a))
print(id(a))

b = 10
c = 20
d = c > b
print(d)
print(type(d))

# Internally for True and False, it is stored as 1 and 0.
# So, if we perform any arithmetic operation on the Boolean values. It is valid and should work.
print(True+True)
print(True+False)
print(True-False)
print(False+False)
