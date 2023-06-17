# Binary Search Using Recursion
def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst)//2
        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                # Here, the original list will get converted into sub-list.
                return recursive_binary_search(lst[midpoint+1:], target)
            else:
                # Here, the original list will get converted into sub-list.
                return recursive_binary_search(lst[:midpoint], target)


def verify(flag):
    print('Target found :', flag)


num_lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = recursive_binary_search(num_lst, -1)
verify(result)

result = recursive_binary_search(num_lst, 1)
verify(result)

result = recursive_binary_search(num_lst, 0)
verify(result)

result = recursive_binary_search(num_lst, 12)
verify(result)

result = recursive_binary_search(num_lst, 100)
verify(result)

result = recursive_binary_search(num_lst, 40)
verify(result)

num_lst1 = []
result = recursive_binary_search(num_lst1, 40)
verify(result)
