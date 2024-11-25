def digits_single(num):
    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
    return num

request = int(input("Введите число: "))
result = digits_single(request)
print(result)
