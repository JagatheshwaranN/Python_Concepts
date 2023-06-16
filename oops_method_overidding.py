class Person:
    def __init__(self, first_name, last_name):
        print("Person class init method")
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print("Person class print method")
        print(self.first_name, self.last_name)


class Employee(Person):

    def __init__(self, first_name, last_name):
        print("Employee class init method")
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print("Employee class print method")
        print(self.first_name, self.last_name)


employee1 = Person('Jack', 'Daniels')
employee1.print_name()


employee2 = Employee('Jack', 'Daniels')
employee2.print_name()
