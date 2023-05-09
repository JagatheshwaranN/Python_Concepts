# To represent a group of objects as a single entity we have to go for Collection Data Types.
# List - It is a collection datatype in Python.

# Characteristics of List
# 1.	Order is important. Insertion order is preserved.
# 2.	Duplicates are allowed.
# 3.	List can be represented using [].
# 4.	Heterogeneous objects are allowed.
# 5.	Indexing and slicing are allowed on list.
# 6.	List is growable in nature.
# 7.	List is mutable object.

listVal = [1, 2, 3, 4, 5]
print(listVal)
print(id(listVal))
print(type(listVal))

# List Value Replace with Heterogeneous Object
listVal[1] = 'a'
print(listVal)

# List Append
listVal.append('b')
print(listVal)

# List Remove
listVal.remove(5)
print(listVal)

# List Indexing
print(listVal[0])
print(listVal[-1])

# List Slicing
print(listVal[1:4])

# List Duplicate
listVal.append(4)
print(listVal)
