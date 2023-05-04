# The process of converting the one type of value to another type value is called as Type Casting.
# int () method is used to convert other forms into int type.

# Float to Int
# When we convert float value to int value, the values after decimal point will be removed.
print(int(123.45))

# Complex to Int
# Complex value can’t be converted to Int value. If we try to convert and will get Type Error.
# print(int(10+20j))  #Type Error

# Bool to Int
print(int(True))
print(int(False))

# Str to Int
# String internally contains only integral values and which is of base 10.
print(int('5'))
# print(int('10.5'))  # Value Error
# print(int('0B111'))  # Value Error

