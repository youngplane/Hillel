import random

random_list = [random.randint(1, 99) for _ in range(random.randint(3, 10))]
print("First list:", random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]
print("Final list:", new_list)
