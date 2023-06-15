# Typical method overloading is not possible in Python as we do in Java. But, we have a workaround.
class MethodOverloading:

    # def sum(self, num1, num2):
    #     print(num1 + num2)

    def sum(self, num1=None, num2=None, num3=None):
        if num1 is not None and num2 is not None and num3 is not None:
            print(num1 + num2 + num3)
        elif num1 is not None and num2 is not None:
            print(num1 + num2)


mo = MethodOverloading()
mo.sum(10, 20)  # TypeError: sum() missing 1 required positional argument: 'num3'
mo.sum(10, 20, 30)
