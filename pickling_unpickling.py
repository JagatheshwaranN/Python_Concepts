# Pickling
# ========
# The process of writing the state of the object into the file is called as Pickling.

# Unpickling
# ==========
# The process of reading an object from the file is called as Unpickling.

# To perform the pickling/unpickling operations we have a module in Python is called as Pickle.
# Pickling => pickle.dump(object, file)
# Unpickling => pickle.load(file)

import pickle


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return 'Hello {}, your age is {}'.format(self.name, self.age)


# pickling
with open("person.txt", "wb") as file:
    person = Person('John', 29)
    pickle.dump(person, file)
    print("Pickling of person object is completed")

# unpickling
with open("person.txt", "rb") as file:
    obj = pickle.load(file)
    print("Person information after unpickling")
    print(obj.display_info())
