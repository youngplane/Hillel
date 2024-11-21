while True:
    # Запрос_0
    number1 = float(input("Введите Ваше первое число: "))
    decision = input("Что вы хотите сделать? (+, -, *, /): ")
    number2 = float(input("Введите Ваше второе число: "))

    # Операции и чек на 0
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
            print("На ноль поделиться не получится!")
    else:
        print("Неверная операция. Попробуйте снова.")

    # Запрос_1
    continue_calculator = input("Хотите продолжить? (y/yes для продолжения): ").lower()
    if continue_calculator not in ("y", "yes"):
        print("Работа калькулятора завершена. Спасибо!")
        break
