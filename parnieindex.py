def sum_and_multiply(lst):
    return sum(lst[::2]) * lst[-1] if lst else 0

ournumbers = [1, 8, 3]
print(sum_and_multiply(ournumbers))
