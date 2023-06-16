class Duck:
    def sound(self):
        print("Quake Quake")


class Cat:
    def sound(self):
        print("Meow Meow")


class Test:
    def execute(self, obj):
        return obj.sound()


test = Test()

duck = Duck()
test.execute(duck)

cat = Cat()
test.execute(cat)