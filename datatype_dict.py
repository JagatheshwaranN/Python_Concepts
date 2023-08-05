# To represent a group of objects as single entity we have to go for Collection Data Types.
# If we want to represent a group of objects as key value pair then we can use Dict.

# Characteristics of Dict
# 1.	Dict can be represented using {K:V}
# 2.	Order is not preserved
# 3. 	Duplicate key not allowed whereas duplicate values are allowed
# 4.	Heterogeneous objects are allowed
# 5.	Dict is mutable object
# 6.	Index and Slice are not applicable

dictVal = {101: 'Alex', 102: 'John'}
print(dictVal)
print(id(dictVal))
print(type(dictVal))

# Dict Add Values
dcVal = {}
dcVal[1] = 'John'
dcVal[2] = 'Alex'
print(dcVal)

# Dict Replace Value
dcVal[1] = 'Blake'
print(dcVal)

# Dict Remove Value
dcVal.pop(1)
print(dcVal)

# Dict Get Keys
print(dictVal.keys())

# Dict Get Values
print(dictVal.values())

# Dict Get Object
print(dictVal.get(101))

# Dict Copy
d = dictVal.copy()
print(d)

dct = dict(dictVal)
print(dct)

# Dict Clear
print(d.clear())

# Dict Items
print(dictVal.items())

# Dict - Update
dictVal.update({103: 'Jenni'})
print(dictVal)

dictVal.update({102: 'Blake'})
print(dictVal)

# Dict - Add
dictVal[104] = 'Erica'
print(dictVal)

# Dict - remove using PopItem
dictVal.popitem()
print(dictVal)

# Dict - Delete the item from the Dictionary
del dictVal[103]
print(dictVal)

# del dictVal

# Iterate through Dict
for key in dictVal.keys():
    print(key)

for key in dictVal.keys():
    print(dictVal[key])

for value in dictVal.values():
    print(value)

# Dict - To print the Dict items using for loop
for key, value in dictVal.items():
    print(key, value)

# Nested Dict

# Creation Approach 1
employees1 = {
    'emp1': {
        'name': 'john',
    },
    'emp2': {
        'name': 'alex'
    }
}
print(employees1)

# Creation Approach 2
emp3 = {'name': 'jenni'}
emp4 = {'name': 'erica'}
employees2 = {
    'emp3': emp3,
    'emp4': emp4
}
print(employees2)

# To Iterate the Nested Dict
for key, value in employees2.items():
    print(key, ' : ', value)

# Dictionary Creation Approaches
d1 = dict({100: 'john'})
print(d1)

# d = dict(list or set or tuple of tuples)
d2 = dict([(100, 'alex')])
print(d2)

d3 = dict(((100, 'alex'), (101, 'john')))
print(d3)

d4 = dict({(100, 'alex'), (101, 'john')})
print(d4)

# d5 = dict({[100, 'alex'], [101, 'john']}) - Not Allowed

# Default Value Set and Get
d3 = dict(((100, 'alex'), (101, 'john')))
print(d3.get(500))  # Key is not available so returning None
print(d3.get(500, 'Default'))  # Key is not available But setting and getting Default value
