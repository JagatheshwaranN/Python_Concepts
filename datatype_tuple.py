# To represent a group of objects as a single entity we have to go for Collection Data Types.
# Tuple - It is a collection datatype in Python.
# Tuple is same as List with one exception as Tuple is immutable. Tuple is also known as read only version of List.

# Characteristics of Tuple
# 1.	Order is important. Insertion order is preserved.
# 2.	Duplicates are allowed.
# 3.	Tuple can be represented using ().
# 4. 	Heterogeneous objects are allowed.
# 5.	Indexing and slicing are allowed on tuple.
# 6.	Tuple is not growable in nature.
# 7.	Tuple is immutable object.

tupVal = (1, 2, 3, 4, 5, 'a')
print(tupVal)
print(id(tupVal))

# Tuple Value Replace with Heterogeneous Object - Not Allowed
# tupVal[1] = 'b'  # TypeError: 'tuple' object does not support item assignment

# Tuple Indexing
print(tupVal[0])
print(tupVal[-1])

# Tuple Slicing
print(tupVal[1:4])

# Tuple Points to Remember
tupleDT = ()
print(tupleDT)
print(type(tupleDT))  # <class 'tuple'>

# In python, it is considered as Int as the value 10 is enclosed with in the braces.
tupleDT = (10)
print(tupleDT)
print(type(tupleDT))  # <class 'int'>

# To make PVM to understand the above statement as tuple and not as int type.
# we have to add the ',' (comma) after the value as below.
tupleDT = (10,)
print(tupleDT)
print(type(tupleDT))





