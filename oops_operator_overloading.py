print(10 + 20)
print('Hello ' + 'World')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


point1 = Point(1, 2)
point2 = Point(3, 4)

# Without operator overloading
# print(point1 + point2) # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

# With operator overloading
print(point1 + point2)
