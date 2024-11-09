def move_last_to_first(lst):
    return [lst[-1]] + lst[:-1] if lst else lst

#проверка
test_list = [16, 6, 8, 13]
print(move_last_to_first(test_list))
