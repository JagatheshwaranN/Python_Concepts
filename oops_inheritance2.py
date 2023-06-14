class Person:
    def __init__(self, first_name, last_name):
        print("Person class init method")
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print("Person class print method")
        print(self.first_name, self.last_name)


class Employee(Person):

    def __init__(self, first_name, last_name, city):
        print("Employee class init method")
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def print_name(self):
        print("Employee class print method")
        print(self.first_name, self.last_name, self.city)


employee = Employee('Jack', 'Daniels', 'Texas')
employee.print_name()

