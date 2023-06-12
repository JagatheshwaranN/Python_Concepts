class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return 'Hello {}, your age is {}'.format(self.name, self.age)


# Create Object for Class and Call method
person1 = Person('John', 29)
print(person1.display_info())

person2 = Person('Erica', 27)
print(person2.display_info())

# Update the property of class using object and call method with updated property
person2.name = 'Jenni'
print(person2.display_info())

# Delete object property
del person2.name
# print(person2.display_info())

# Delete Object
del person2
# print(person2)
