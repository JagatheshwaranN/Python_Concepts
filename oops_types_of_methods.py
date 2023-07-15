# In Python, we have 3 types of methods as below,
# 1.	Instance Method (Object level method)
# 2.	Class Method (Class level method)
# 3.	Static Method (General utility method)

# Points about Methods
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
