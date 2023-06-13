# MRO - If a class extends more than one class and if we try to call the super class constructor then in this case
# we have two Parent classes and here which super class will get execute is based on method resolution order and which
# from left to right.
class Parent:
    pt_data = 10

    def __init__(self):
        print("Init from Parent")

    def pt_method1(self):
        print("Parent Class Method1")

    def pt_method2(self):
        print("Parent Class Method2")


class Child:
    cd_data = 20

    def __init__(self):
        print("Init from Child")

    def cd_method1(self):
        print("Child Class Method1")

    def cd_method2(self):
        print("Child Class Method2")


class GrandChild(Parent, Child):
    gc_data = 30

    def __init__(self):
        super().__init__()
        print("Init from GrandChild")

    def gc_method1(self):
        print("Grand Child Method1")

    def gc_method2(self):
        print("Grand Child Method2")


grandchild = GrandChild()
print(grandchild.pt_data)
print(grandchild.cd_data)
print(grandchild.gc_data)
grandchild.pt_method1()
grandchild.cd_method2()
grandchild.gc_method1()
