# In python, an iterator is an object and which contains the countable number of values.
# It can be iterated up on the value.

lst = [1, 2, 3]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) - StopIteration

print("========================================")

# Here, the for loop internally uses the iter object to iterate the values.
for i in lst:
    print(i)

print("========================================")


class MyIterator:

    def __iter__(self):
        self.counter = 1
        return self

    def __next__(self):
        if self.counter <= 50:
            next_counter = self.counter
            self.counter += 1
            return next_counter
        else:
            raise StopIteration


myIterator = MyIterator()
itr = iter(myIterator)
for v in itr:
    print(v)
