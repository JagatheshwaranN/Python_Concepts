# A number with both real and imaginary parts are called as Complex data type.
# syntax is a+bj (Here the imaginary part is represented using the value j)

x = 10+20j
print(x)
print(type(x))
print(id(x))
print(x.real)
print(x.imag)

# We can have different combination in complex numbers as below.
a = 10+20j
b = 10.5+20j
c = 10+20.5j
print(a)
print(b)
print(c)

# The real part of the complex number can be represented in the binary, octal and hexadecimal forms
# whereas the imaginary part we should represent only in decimal form.
d = 0b111+10j
e = 0o12+20j
f = 0xab+30j
print(d)
print(e)
print(f)

# We can perform arithmetic operations between two complex numbers.
# x+y, x-y, x*y and x/y
x = 10+20j
y = 20+30j
print(x+y)
print(x-y)
print(x*y)
print(y/x)

