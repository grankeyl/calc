def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            print("\nВыберите операцию:")
            print("1. Сложение (+)")
            print("2. Вычитание (-)")
            print("3. Умножение (*)")
            print("4. Деление (/)")
            print("5. Возведение в степень (**)")
            print("6. Извлечение корня (√)")
            print("0. Выход")

            choice = input("Введите номер операции: ")

            if choice == "0":
                print("Выход из программы.")
                break

            if choice == "1":
                result = num1 + num2
                print(f"Результат: {result}")
            elif choice == "2":
                result = num1 - num2
                print(f"Результат: {result}")
            elif choice == "3":
                result = num1 * num2
                print(f"Результат: {result}")
            elif choice == "4":
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    result = num1 / num2
                    print(f"Результат: {result}")
            elif choice == "5":
                result = num1 ** num2
                print(f"Результат: {result}")
            elif choice == "6":
                if num1 < 0 or num2 <= 0:
                    print("Ошибка: для корня числа должны быть положительными.")
                else:
                    result1 = num1 ** (1 / num2)
                    print(f"Результат: {result1}")
            else:
                print("Некорректный выбор операции.")
        
        except ValueError:
            print("Ошибка: нужно ввести число.")

        print("\n---\n")

calculator()