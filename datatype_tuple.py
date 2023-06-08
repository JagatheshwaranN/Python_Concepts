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
print(type(tupVal))

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

# Str to Tuple
print(tuple('python'))

# Verify Tuple Element Present
fruits = ('apple', 'banana', 'mango', 'grapes')
if 'mango' in fruits:
    print('Yes, mango available in the fruits tuple')

# Tuple - Update Item - Tuple to List Conversion
# By default, we can't update the tuple element as it's immutable in nature. But, we have a workaround
# to convert the tuple to list and update the same and then convert it back to tuple using constructor.

fruits = ('apple', 'banana', 'mango', 'grapes')
print(fruits)
lst = list(fruits)
lst[1] = 'berry'
fruits = tuple(lst)
print(fruits)

# Tuple - Add Item
fruits = ('apple', 'banana', 'mango', 'grapes')
print(fruits)
lst = list(fruits)
lst.append('pineapple')
fruits = tuple(lst)
print(fruits)

# Tuple - Remove Item
fruits = ('apple', 'banana', 'mango', 'grapes')
print(fruits)
lst = list(fruits)
lst.remove('grapes')
fruits = tuple(lst)
print(fruits)

# Pack and Unpack Tuples

# When we create tuple, we used to add some items into the tuple and assign it to some variable.
# This process is called as Packing a tuple.
fruits = ('apple', 'banana')  # Tuple Packing

# Collecting the tuple elements in a variable is called as Tuple Unpacking.
f1, f2 = fruits
print(f1)
print(f2)

# In case, if we don't know the variable size to hold the tuple values, we can use * with last variable, and it
# will take remaining values of tuple as list into the last variable.
fruits = ('apple', 'banana', 'mango', 'grapes')
f1, f2, *f3 = fruits
print(f1)
print(f2)
print(f3)

# Iterate through Tuple

fruits = ('apple', 'banana', 'mango', 'grapes')

# Approach 1
for item in fruits:
    print(item)

print("=======================================")

# Approach 2
for index in range(len(fruits)):
    print(fruits[index])

print("=======================================")

# Approach 3
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Join Two Tuples
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8)
t3 = t1 + t2
print(t3)

# Multiply Tuple
t4 = ('SA', 'RE', 'GA', 'MA') * 2
print(t4)

# Count number of occurrence of Element in a Tuple
t5 = (1, 2, 3, 1, 2, 1, 3, 4, 2, 5, 6, 7, 8)
print(t5.count(2))

# Find first occurrence of an element in a Tuple
t6 = (1, 2, 3, 1, 2, 1, 3, 4, 5, 6, 4, 7, 8)
print(t5.index(4))

