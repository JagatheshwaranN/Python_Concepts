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

# List Comprehension
fruits = ['Apple', 'Mango', 'Grapes', 'Kiwi', 'Orange']

# Generate SubList without using List Comprehension
new_fruits = []
for f in fruits:
    if 'a' in f:
        new_fruits.append(f)

print(new_fruits)

# Generate SubList using List Comprehension
new_fruits = [f for f in fruits if 'a' in f]
print(new_fruits)

# List Comprehension with Range function
lst6 = [f for f in range(10)]
print(lst6)

# List Comprehension to update all list element as same value
new_fruits = ['fruits' for f in fruits if 'a' in f]
print(new_fruits)

# List Sorting
fruits = ['Apple', 'Mango', 'Grapes', 'Kiwi', 'Orange']

# Ascending Order
fruits.sort()
print(fruits)

# Descending Order
fruits.sort(reverse=True)
print(fruits)

# Case Insensitive Sort
fruits_ext = ['Apple', 'Mango', 'Grapes', 'Kiwi', 'Orange', 'banana', 'guava']

fruits_ext.sort()
print(fruits_ext)

fruits_ext.sort(key=str.lower)
print(fruits_ext)

numbers = [20, 10, 50, 40, 30, 70, 60]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


def my_logic(num):
    return abs(num - 100)


numbers.sort(key=my_logic)
print(numbers)

# List Reverse
fruits_ext = ['Apple', 'Mango', 'Grapes', 'Kiwi', 'Orange', 'banana', 'guava']
fruits_ext.reverse()
print(fruits_ext)

# List Copy
lst7 = ['sa', 're', 'ga', 'ma']
lst8 = lst7.copy()
print(lst8)

# List Join / Concatenation
lst9 = [1, 2, 3, 4, 5]
lst10 = [6, 7, 8]
lst11 = lst9 + lst10
print(lst11)

# List Comparison
# Object1 == Object2
# 1. The number of elements must be equal
# 2. The order should be same
# 3. The contents should be same (including case)

lst21 = ['dog', 'cat']
lst22 = ['dog', 'cat']
lst23 = ['DOG', 'CAT']
print(lst21 == lst22)
print(lst22 == lst23)
print(lst21 != lst23)

# Object1 is Object2
# The id(address) of lst21 and lst22 are different
print(lst21 is lst22)  # False

# Difference is vs ==
# 1. Is operator checks for address comparison
# 2. == operator checks for content comparison

print(lst21[0] is lst22[0])  # True - String comparison, Immutable objects and reused

lst24 = [50, 100, 300]
lst25 = [40, 90, 200]
lst26 = [50, 90, 200]
print(lst24 > lst25)
print(lst24 >= lst26)
print(lst25 > lst26)
