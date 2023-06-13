class Parent:
    pt_data = 10

    def pt_method1(self):
        print("Parent Class Method1")

    def pt_method2(self):
        print("Parent Class Method2")


class Child(Parent):
    cd_data = 20

    def cd_method1(self):
        print("Child Class Method1")

    def cd_method2(self):
        print("Child Class Method2")


child = Child()
print(child.cd_data)
print(child.pt_data)
child.cd_method1()
child.pt_method2()


class GrandChild(Child, Parent):
    gc_data = 30

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
