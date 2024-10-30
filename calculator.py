#запрос
number1 = float(input("Введите Ваше первое число: "))
decision = input("Что вы хотите сделать? (+, -, *, /): ")
number2 = float(input("Введите Ваше второе число: "))

#операции и чек на 0
if decision == "+":
    print("Ваш результат: ", number1 + number2)
elif decision == "-":
    print("Ваш результат: ", number1 - number2)
elif decision == "*":
    print("Ваш результат:", number1 * number2)
elif decision == "/":
        if number2 != 0:
            print("Ваш результат: ", number1 / number2)
        else:
            print("На ноль поделиться не получиться!")
