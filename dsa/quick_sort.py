def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        less_than_pivot = []
        greater_than_pivot = []
        pivot = lst[0]
        for item in lst[1:]:
            if item <= pivot:
                less_than_pivot.append(item)
            else:
                greater_than_pivot.append(item)
        # print("%15s %1s %-15s" %(less_than_pivot, pivot, greater_than_pivot))
        return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)


lst_values = [8, 10, 5, 4, 1, 2, 70]
print(quick_sort(lst_values))
