request_number = int(input("Добро пожаловать! Введите 5-значное число: "))

# Ввод цифр с использованием деления и остатка от деления
box1 = request_number // 10000
box2 = (request_number // 1000) % 10
box3 = (request_number // 100) % 10
box4 = (request_number // 10) % 10
box5 = request_number % 10

print(f"{box5}{box4}{box3}{box2}{box1}")