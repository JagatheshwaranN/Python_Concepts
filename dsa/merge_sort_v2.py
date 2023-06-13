def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid_index = len(lst) // 2
        left_half = merge_sort(lst[:mid_index])
        right_half = merge_sort(lst[mid_index:])
        print("%15s %-15s" % (left_half, right_half))
        sorted_list = []
        left_index = 0
        right_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                sorted_list.append(left_half[left_index])
                left_index += 1
            else:
                sorted_list.append(right_half[right_index])
                right_index += 1
        sorted_list += left_half[left_index:]
        sorted_list += right_half[right_index:]
        return sorted_list


alist = [50, 23, 67, 87, 72, 94, 17, 33, 42]
print(merge_sort(alist))
