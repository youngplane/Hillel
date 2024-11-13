def move_zeros_to_end(lst):
    return [num for num in lst if num != 0] + [0] * lst.count(0)

# ввод нашего числа
ournumbers = [5, 0, 0, 8, 0, 4]

print(move_zeros_to_end(ournumbers))
