# The process of converting the one type of value to another type value is called as Type Casting.
# complex () method is used to convert other forms into complex type.
# To convert from other type value to complex type value, we have following two forms.
# 1. complex (x) => only real value
# 2. complex (x, y) => both real and imaginary values

# Int to Complex
print(complex(10))
print(complex(0b111))
print(complex(0x123))
print(complex(10, 20))

# Float to Complex
print(complex(10.5))
print(complex(10.5, 5.5))

# Bool to Complex
print(complex(True))
print(complex(False))

# Str to Complex
print(complex("10"))
print(complex("5.5"))
# print(complex("0B111"))  # Type Error
# print(complex("10", "20"))  # TypeError: complex() can't take second arg if first is a string
# print(complex(10, "20"))  # TypeError: complex() second arg can't be a string


