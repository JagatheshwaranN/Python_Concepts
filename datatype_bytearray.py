# To represent a group of objects as a single entity we have to go for Collection Data Types.
# If we want to represent a group of byte values then we can go for Bytes data type.
# ByteArray is similar to Bytes data type with one exception as Bytes Array is mutable object.

# Characteristics of ByteArray
# 1.	Byte Array data type can use values only from 0 to 255.
#       (If value higher than 255 taken, value error will be thrown)
# 2.	Byte Array data type is mutable object.
# 3.	Index and Slice operations are applicable.

barr = [10, 20, 30, 40, 50]
b = bytearray(barr)
print(b)
for x in b:
    print(x)
print(id(b))
print(type(b))

# ByteArray Update
barr[1] = 25
b = bytearray(barr)
for x in b:
    print(x)

b[2] = 35
for x in b:
    print(x)

# ByteArray Indexing
print(b[1])
print(b[-1])

# ByteArray Slicing
b1 = b[1:4]
for x1 in b1:
    print(x1)

# ByteArray Append
b1.append(60)
for x1 in b1:
    print(x1)

# ByteArray Copy
b2 = b1.copy()
for x2 in b2:
    print(x2)

# ByteArray Insert
b2.insert(2, 70)
for x2 in b2:
    print(x2)

