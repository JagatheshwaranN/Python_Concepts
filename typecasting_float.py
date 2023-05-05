# The process of converting the one type of value to another type value is called as Type Casting.
# float () method is used to convert other forms into float type.

# Int to Float
print(float(5))
print(float(0B111))
print(float(0O12))
print(float(0X123))

# Complex to Float
# Complex value can’t be converted to Float value. If we try to convert and will get Type Error.
# print(float(10+20j))  #Type Error

# Bool to Float
print(float(True))
print(float(False))

# Str to Float
# String internally contains only integral values / float values and which is of base 10.
print(float('10'))
print(float('5.0'))

