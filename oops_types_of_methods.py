# In Python, we have 3 types of methods as below,
# 1.	Instance Method (Object level method)
# 2.	Class Method (Class level method)
# 3.	Static Method (General utility method)

# Points about Methods
# ====================
# 1.	If we are accessing the instance variable ( whether using the static and local variables
#       or not.)
# 2.	The first argument to the instance method should be self.
# 3.	If we are not using any instance variable, then we can go for Class or Static method.
# 4.	If we are not using any instance variable and if we are using static variable, then its
#       Class method.
# 5.	If we are not using any instance variable and static variable, then this method is no way
#       related to object and class and its general utility method. We have to declare such method
#       as Static method.
# 6.	In Python, For every class, a class level object (cls) is created to hold the class level
#       variables.
# 7.	In python, if we want to access the class level variables, then we should use cls reference.
# 8.	We have to use @classmethod decorator to inform PVM that the method is class method.

# Method Usage Tricks
# ===================
# 1.	Instance variable + Class variable + Local variable => Instance Method
# 2.	Static variable + Local variable => Class Method
# 3.	Local Variable => Static Method

class Test:
    @classmethod
    def method1(cls):
        print(id(cls))
        print(id(Test))


Test.method1()


class Student:
    collegeName = 'ABC College'
    principal = "John"

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def get_student_info(self):
        print('Student Name   :', self.name)
        print('Student Roll   :', self.rollno)

    @classmethod
    def get_college_info(cls):
        print("College Name   :", cls.collegeName)
        print("Principal Name :", cls.principal)

    @staticmethod
    def get_student_mark_avg(m1, m2, m3):
        return (m1 + m2 + m3) / 3


student = Student('Alex', 101)
student.get_college_info()
student.get_student_info()
print("Student Mark   :", student.get_student_mark_avg(98, 97, 99))
