# To represent a group of objects as a single entity we have to go for Collection Data Types.
# If we want to represent a group of byte values then we can go for Bytes data type.

# Characteristics of Bytes
# 1.	Bytes data type can use values only from 0 to 255. (If value higher than 255 taken, value error will be thrown)
# 2.	Bytes data type is immutable object.
# 3.	Index and Slice operations are applicable.

bt = [10, 20, 30, 40, 50]
b = bytes(bt)
for x in b:
    print(x)
print(b)
print(id(b))
print(type(b))

# Bytes Update - Not Applicable
# b[0] = 55  # TypeError: 'bytes' object does not support item assignment

# Bytes Indexing
print(b[0])
print(b[-1])

# Bytes Slicing
b1 = b[1:3]
for x1 in b1:
    print(x1)
