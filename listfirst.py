your_list = [5, 1, 11, 6]

if len(your_list) > 1:
    result = [your_list[-1]] + your_list[:-1]
else:
    result = your_list

print("Результат:", result)
