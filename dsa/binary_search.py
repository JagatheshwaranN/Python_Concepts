# Binary Search
def binary_search(lst, target):
    first = 0
    last = len(lst)-1
    while first <= last:
        midpoint = (first+last)//2
        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None


def verify(index):
    if index is not None:
        print('Target found at index :', index)
    else:
        print('Target not found in the list')


num_lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# num_lst = [50, 20, 30, 60, 10, 40, 70, 80, 90, 100] - Working
# num_lst = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] - Not Working

result = binary_search(num_lst, -1)
verify(result)

result = binary_search(num_lst, 1)
verify(result)

result = binary_search(num_lst, 0)
verify(result)

result = binary_search(num_lst, 12)
verify(result)

result = binary_search(num_lst, 100)
verify(result)

result = binary_search(num_lst, 40)
verify(result)
