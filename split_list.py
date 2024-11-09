def split_list(lst):
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

#проверка
print(split_list([4, 5, 6, 7, 8, 9]))
print(split_list([4, 5, 6]))
print(split_list([4, 5, 6, 7, 8]))
print(split_list([4]))
print(split_list([]))

