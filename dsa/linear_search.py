# Linear Search
def linear_search(lst, target):
    for n in range(0, len(lst)):
        if lst[n] == target:
            return n
    return None


def verify(index):
    if index is not None:
        print("Target is found at index :", index)
    else:
        print("Target not found in the list")


# num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = linear_search(num_lst, -1)
verify(result)

result = linear_search(num_lst, 0)
verify(result)

result = linear_search(num_lst, 12)
verify(result)

result = linear_search(num_lst, 70)
verify(result)
