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

# Str to List
print(list('python'))

# List Size
print(len(listVal))

# List with mixed Data types
person_lst = ['john', 20, 200000.00, True]
print(person_lst)

# List Creation with Constructor
fruits = list(('apple', 'orange', 'mango'))
print(fruits)

# Check List Value
if 'apple' in fruits:
    print("Yes, apple is in fruits list")
else:
    print("No, Apple is not in fruits lists")

# List Update with Range of Values
alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(alpha_lst)

alpha_lst[1:3] = ['x', 'y']
print(alpha_lst)

alpha_lst[0:1] = ['v', 'w']
print(alpha_lst)

alpha_lst[0:2] = ['a']
print(alpha_lst)

# Insert Into List
alpha_lst.insert(len(alpha_lst), 'g')
print(alpha_lst)

# Merge List

# List with List
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8]
lst1.extend(lst2)
print(lst1)
print(lst2)

# Tuple with List
lst1.extend(('t1', 't2'))
print(lst1)

# Set with List
lst1.extend({'s1', 's2'})
print(lst1)

# Dictionary with List
# When we try to add the dictionary then only the key of the dictionary will get added to the list.
dct = {
    'topic': 'list'
}
lst1.extend(dct)
print(lst1)

# Remove List Items using Index
# Pop method have advantage of showing the element which is getting deleted from the list over the remove method.
# Remove method don't have the option to show the element which is getting deleted.
lst3 = ['A', 'B', 'C', 'D', 'E']

lst3.pop()
print(lst3)

value = lst3.pop(3)
print(value)
print(lst3)

# Remove List Items using Del
lst4 = ['A', 'B', 'C', 'D', 'E']
del lst4[0]
print(lst4)

# Remove List Items using clear
lst5 = ['A', 'B', 'C', 'D', 'E']
lst5.clear()
print(lst5)