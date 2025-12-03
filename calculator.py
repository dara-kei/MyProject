def calculator():
    while True:
        num1 = input("Enter first number: or q to quit: ")


       # Проверка выхода
        if num1 == "q":
            print("Calculator closed")
            break


        # Проверка корректного введения первого числа
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid first number")
            continue


        num2 = input("Enter second number: ")

        # Проверка корректного введения второго числа
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid second number")
            continue


        operator = input("Enter operator (+, -, *, /, **): ")
        res = 0


        # Проверка оператора
        if operator not in ["+", "-", "*", "/", "**"]:
            print("Unknown operator")
            continue


        # Вычисления
        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Impossible to divide by zero")
                continue
            else:
                res = num1 / num2
        elif operator == '**':
            res = num1 ** num2


        # Вывод результата
        if num1.is_integer() and num2.is_integer():
            print(f"{int(num1)} {operator} {int(num2)} = {int(res)}")
        elif res.is_integer():
            print(f"{(num1)} {operator} {(num2)} = {int(res)}")
        else:
            print(f"{(num1)} {operator} {(num2)} = {res:.2f}")


calculator()
