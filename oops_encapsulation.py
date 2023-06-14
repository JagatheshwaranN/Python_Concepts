class Person:

    def __init__(self, name, age, _city, __stay):
        self.name = name
        self.age = age  # Public Variable
        self._city = _city  # Protected Variable
        self.__stay = __stay  # Private Variable

    def display_info(self):
        self.__private_method()
        return 'Hello, your name is {} and your age is {} ' \
               'and you are from {} and you will stay here {} days'.format(self.name, self.age, self._city, self.__stay)

    @property
    def city(self):
        return self._city

    def set_stay(self, stay):
        self.__stay = stay

    def get_stay(self):
        return self.__stay

    def __private_method(self):
        print("Private Method Demo")


# Create Object for a Class and Call the method
person1 = Person('John', 29, 'Texas', 3)

# Approach 1
print(person1.display_info())

# Approach 2
print('Hello, your name is {} and your age is {} and you are from {} ' 
      'and you will stay here {} days'.format(person1.name, person1.age, person1.city, person1.get_stay()))
