# In python, we have try and except keywords, which is used to handle the exception.

name = input("Enter your name : ")
age = input("Enter your age : ")
try:
    print("Hello {}, you are {} years old".format(name, int(age)))
except ValueError:
    print("Please enter value age : ", age)
