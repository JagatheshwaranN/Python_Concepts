# The yield function internally uses the iterator concepts.

def my_generator():
    yield 10
    yield 20


values = my_generator()
print(values)
print(values.__next__())
print(values.__next__())

print("=========================================")

values = my_generator()

for i in values:
    print(i)

print("=========================================")


def my_generator2():
    n = 1
    while n <= 5:
        cube = n*n*n
        yield cube
        n = n+1


values = my_generator2()

for v in values:
    print(v)
