# To represent a group of objects as a single entity we have to go for Collection Data Types.
# When we want to represent a sequence of numbers then we can go for Range data type.

# Characteristics of Range
# 1.	We have 3 forms of range data type.
# 2.	Order is preserved.
# 3.	Index and Slice operators are applicable.
# 4.	Range is immutable object.

# Form1 range(n) -> from 0 to n-1
r = range(10)
print(r)
print(id(r))
print(type(r))

for x in r:
    print(x)

# Form2 range(begin, end) -> begin to end-1
r = range(1, 10)
for x in r:
    print(x)

# Form3 range(begin, end, inc/dec)
r = range(1, 20, 2)
for x in r:
    print(x)

# Range Indexing
r = range(1, 10)
print(r[0])
print(r[-1])

# Range Slicing
r1 = r[1:5]
for x1 in r1:
    print(x1)

# Range Update - Not Applicable
# r[1] = 1000  # TypeError: 'range' object does not support item assignment
