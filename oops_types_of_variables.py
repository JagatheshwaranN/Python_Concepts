# In Python, we have 3 types of variables as below,
# 1.	Instance Variables (Object level variables)
# 2.	Static Variables (Class level variables)
# 3.	Local Variables (Method level variables)

# Reference variable can be used to refer the objects. By using reference variable, we can invoke
# functionality of the object. For a single object, there may be a chance of multiple references.
# For any class, we can take any number of objects (one to many)
# For any object, we can take any number of reference variables (one to many)

# Instance Variable
# =================
# 1.	If the value of the variable is varied from object to object, such type of variables
#       is called as Instance Variables.
# 2.	For every object a separate copy will be created.
# 3.	In general, we can define instance variables inside Constructor using Self object.
# 4.	We can declare the Instance variable inside Instance Method using self.
# 5.	We can declare the Instance variable outside of Class by using object reference.

class Instance:

    def __init__(self):
        self.x1 = 10
        print("X1 :", self.x1)

    def instance_variable_demo(self):
        self.x2 = 20
        print("X2 :", self.x2)


instance = Instance()
instance.instance_variable_demo()
instance.x3 = 30
print("X3 :", instance.x3)


# Static Variables
# ================
# 1.	If the value of the variable is NOT varied from object to object, then it’s not
#       recommended to declare that variable as Instance variable. We should declare it
#       as Static variables.
# 2.	In case of Static variable, a single copy will be created and shared by every
#       object of the class.
# 3.	Very often, static variables will be declared within the class directly.
# 4.	We can also declare the static variable inside Constructor using Class Name,
#       inside Instance Method using Class Name, inside the Class Method using Class Name
#       & cls reference, and inside the Static Method using Class Name.

class Static:
    y2 = 10

    def __init__(self):
        Static.y1 = 20
        print("Y1 :", Static.y2)

    def static_variable_demo(self):
        Static.y3 = 30
        print("Y3 :", Static.y3)

    @classmethod
    def class_method_demo(cls):
        cls.y4 = 40
        print("Y4 :", cls.y4)
        Static.y5 = 50
        print("Y5 :", Static.y5)

    @staticmethod
    def static_method_demo():
        Static.y6 = 60
        print("Y6 :", Static.y6)


static = Static()
print("Y2 :", Static.y2)
static.static_variable_demo()
static.class_method_demo()
static.static_method_demo()
Static.y7 = 70
print("Y7 :", Static.y7)


# Local Variables
# ===============
# 1.	To meet the temporary requirements of the programmer, we can declare variables directly
#       inside a method, such type of variables is called as Local Variable.
# 2.	Local variables will be created at the time of method execution and destroyed once method
#       completes.
# 3.	Local variables of the method cannot be accessed from outside the method.

class Local:

    def __init__(self):
        pass

    @staticmethod
    def local_variable_demo():
        z1 = 10
        print("Z1 :", z1)


local = Local()
local.local_variable_demo()
