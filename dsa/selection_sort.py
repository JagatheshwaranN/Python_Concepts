def selection_sort(lst):
    sorted_list = []
    # print(" %-25s %-25s " % (lst, sorted_list))
    for index in range(len(lst)):
        index_to_move = index_of_min_value(lst)
        sorted_list.append(lst.pop(index_to_move))
    # print(" %-25s %-25s " % (lst, sorted_list))
    return sorted_list


def index_of_min_value(lst):
    min_index = 0
    for index in range(1, len(lst)):
        if lst[index] < lst[min_index]:
            min_index = index
    return min_index


lst_values = [8, 10, 5, 4, 1, 2, 70]
print(selection_sort(lst_values))
