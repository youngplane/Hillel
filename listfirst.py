def move_last_to_first(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]

your_list = [5, 1, 11, 6]
result = move_last_to_first(your_list)
print("Результат:", result)
