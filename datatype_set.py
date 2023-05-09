# To represent a group of objects as a single entity we have to go for Collection Data Types.
# When we have requirements to display group of values as single entity where duplicates not allowed.
# And order is not important, then we can use Set.
# Set - It is a collection datatype in Python.

# Characteristics of Set
# 1.	Duplicated not allowed.
# 2.	Order is not preserved.
# 3. 	Indexing / Slicing not applicable as order is not preserved.
# 4.	Heterogeneous objects allowed.
# 5.	Set is growable in nature.
# 6.	Set is mutable object.
# 7.	Set can be represented using {}

setVal = {1, 2, 3, 4, 5}
print(setVal)
print(id(setVal))
print(type(setVal))

# Set Add
setVal.add('a')
print(setVal)

# Set Value Replace with Heterogeneous Object
# setVal[1] = 'b'
# print(setVal)  # TypeError: 'set' object does not support item assignment

# Set Remove
setVal.remove('a')
print(setVal)

# Set Indexing
# print(setVal[0])  # TypeError: 'set' object is not subscript-able

# Set Slicing
# print(setVal[1:4])  # TypeError: 'set' object is not subscript-able

# Set Duplicates
setDT = {1, 1, 2, 3, 4, 5}
print(setDT)  # {1, 2, 3, 4, 5} - Set datatype won't accept the duplicate objects.

# Set Points to Remember
setVlDT = {}
print(type(setVlDT))  # <class 'dict'>

# Set is rarely used concept in Python whereas Dict is mostly used concept.
# Hence, we have the type as Dict for above syntax.
# To represent it as Set, we have to explicitly mention the type as below.
setVlDT = set()
print(type(setVlDT))  # <class 'set'>

