import json

# Dict to Json
person_detail = {'name': 'John', 'age': 29}
print(type(person_detail))

print(type(json.dumps(person_detail)))

print(json.dumps(person_detail))

# List to Json
fruit_list = ['apple', 'orange', 'mango']
print(json.dumps(fruit_list))

# Tuple to Json
fruit_tuple = ('apple', 'orange', 'mango')
print(json.dumps(fruit_list))

# String to Json
string = 'Json'
print(json.dumps(string))

# Int to Json
number = 200
print(json.dumps(number))

# Float to Json
decimal_number = 120.65
print(json.dumps(decimal_number))

# Boolean to Json
flag = True
print(json.dumps(flag))

# None to Json
print(json.dumps(None))

# Complex Json Data
person_info = {'name': 'John', 'age': 29,
               'cars': ('Swift', 'Nexus', 'Honda')}

# Json data format
print(json.dumps(person_info, indent=2))

print("=============================================")

# Json data format with Sorted keys
print(json.dumps(person_info, indent=2, sort_keys=True))

print("=============================================")

# Json data format with updated separator
print(json.dumps(person_info, indent=2, separators=(';', "=")))

