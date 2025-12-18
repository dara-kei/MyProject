# 8. Калькулятор с операциями
# Добавить обработку исключений в свой калькулятор.
# Обработать:
# ● Деление на ноль.
# ● Неизвестную операцию (поднять ValueError и поймать её снаружи).
# ● Неверный ввод

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
            raise ValueError(operator)

        # Вычисления
        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        elif operator == '/':
            try:
                res = num1 / num2
            except ZeroDivisionError:
                print("Division by zero")
        elif operator == '**':
            res = num1 ** num2

        # Вывод результата
        if num1.is_integer() and num2.is_integer():
            print(f"{int(num1)} {operator} {int(num2)} = {int(res)}")
        elif res.is_integer():
            print(f"{(num1)} {operator} {(num2)} = {int(res)}")
        else:
            print(f"{(num1)} {operator} {(num2)} = {res:.2f}")

try:
    calculator()
except ValueError as e:
    print(f"Unknown operator: {e}")
