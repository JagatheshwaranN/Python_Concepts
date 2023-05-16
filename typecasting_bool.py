# The process of converting the one type of value to another type value is called as Type Casting.
# bool () method is used to convert other forms into bool type.

# Int to Bool
print(bool(1))
print(bool(0))
print(bool(11))
print(bool(-1))

# Float to Bool
print(bool(1.0))
print(bool(0.0))
print(bool(-1.0))

# Complex to Bool
print(bool(1+0j))
print(bool(0+0j))
print(bool(-1+0j))

# Str to Bool
# If the argument is non-empty then it will consider as True and if its empty then it considered as False.
print(bool('1'))
print(bool(''))
print(bool('True'))
print(bool('False'))
print(bool([]))
print(bool(['AB']))
