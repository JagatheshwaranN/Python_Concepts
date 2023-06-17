# Bogo Sort is the worst case runtime sorting algorithm
import random


def is_sorted(lst):
    for index in range(len(lst)-1):
        if lst[index] > lst[index + 1]:
            return False
    return True


def bogo_sort(lst):
    attempt = 0
    while not is_sorted(lst):
        print(attempt)
        random.shuffle(lst)
        attempt += 1
    return lst


lst_values = [8, 10, 5, 4, 1, 2, 70]
print(bogo_sort(lst_values))
