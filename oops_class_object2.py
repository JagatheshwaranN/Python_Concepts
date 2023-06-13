class Person:

    def __init__(self, name='Great', *param, **kwargs):
        self.name = name
        self.param = param
        self.kwargs = kwargs

    def display_info(self):
        return 'Hello, your name is {} and you have holidays on {} and your details are {}'.format(self.name,
                                                                                                   self.param,
                                                                                                   self.kwargs)


# Create Object for a Class and Call the method
person1 = Person()
print(person1.display_info())

person2 = Person('Erica', 11, 12, 13)
print(person2.display_info())

person3 = Person('John', 11, 12, 13, age=29, city='Texas')
print(person3.display_info())

print(person3.name, person3.param, person3.kwargs)
