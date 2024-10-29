request_number = int(input("Добро пожаловать!Введите 4-х значное число: "))

# Ввод цифер используя деление и остаток от деления
box1 = request_number // 1000
box2 = (request_number // 100) % 10
box3 = (request_number // 10) % 10
box4 = request_number % 10

print(box1)
print(box2)
print(box3)
print(box4)