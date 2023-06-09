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
