# The number without decimal points are called as Integral numbers.
# The long integral values can be represented by Int data type only in Python 3.x
# In Python 2.x, we had long data type to hold long integral values and int data type to hold small integral values.

# Int in decimal form
a = 123
b = 987
print(a)
print(type(a))
print(id(a))

# Int in binary form
c = 0B1111
d = 0b1111
print(c)
print(type(c))
print(id(c))

# Int in octal form
e = 0O123
f = 0o123
print(e)
print(type(e))
print(id(e))

# Int in hexadecimal form
g = 0X123
h = 0x123
i = 0xabc

print(g)
print(type(g))
print(id(g))

print(i)
print(type(i))
print(id(i))

# Base Conversion Functions

# bin() used to convert the other int forms to binary form
print(bin(100))
print(bin(0o123))
print(bin(0xabc))

# oct() used to convert the other int forms to octal form
print(oct(100))
print(oct(0B1111))
print(oct(0xabc))

# hex() used to convert the other int forms to hexadecimal form
print(hex(100))
print(hex(0B1111))
print(hex(0o123))
