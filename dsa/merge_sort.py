def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sub-lists
    Conquer: Recursively sort the sub-lists created in the previous step
    Combine: Merge the sorted sub-lists created in previous step

    Takes O(n log n) time.
    With list slice operation, Takes O(kn log n) time.
    """
    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(lst):
    """
    Divide the unsorted list at midpoint into sub-lists.
    Returns two sub-lists - left and right.
    Over all takes O(log n) time.
    With list slice operation, Over all takes O(k log n) time.
    """
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process.
    Returns a new merged list.
    Runs in overall O(n) time.
    """
    lt = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lt.append(left[i])
            i += 1
        else:
            lt.append(right[j])
            j += 1

    while i < len(left):
        lt.append(left[i])
        i += 1
    while j < len(right):
        lt.append(right[j])
        j += 1

    return lt


def verify_sorted(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return True

    return lst[0] < lst[1] and verify_sorted(lst[1:])


alist = [50, 23, 67, 87, 72, 94, 17, 33, 42]
lstVal = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(lstVal))
