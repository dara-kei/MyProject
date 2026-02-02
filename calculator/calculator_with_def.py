def summary(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

def squaring(num1, num2):
    return num1 ** num2

def input_num(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid number. Try again.")


def input_operator():
    while True:
        op = input("Enter operator (+, -, *, /, **): ")
        if op in ["+", "-", "*", "/", "**"]:
            return op
        else:
            print("Invalid operator. Try again.")


def calculate(num1, num2, operator):
    res = 0

    if operator == '+':
        res = summary(num1, num2)
    elif operator == '-':
        res = subtraction(num1, num2)
    elif operator == '*':
        res = multiplication(num1, num2)
    elif operator == '/':
        res = division(num1, num2)
    elif operator == '**':
        res = squaring(num1, num2)

    return res

def calculator():
    while True:
        ex = input("Press Enter if you want to continue or q if you want to quit: ")
        if ex.lower() == "q":
            break

        num1 = input_num("Enter first number: ")
        num2 = input_num("Enter second number: ")
        operator = input_operator()

        try:
            res = calculate(num1, num2, operator)
        except ZeroDivisionError:
            print("Division by zero!")
            continue

        # Вывод результата
        if num1.is_integer() and num2.is_integer():
            print(f"{int(num1)} {operator} {int(num2)} = {int(res)}")
        elif res.is_integer():
            print(f"{num1} {operator} {num2} = {int(res)}")
        else:
            print(f"{num1} {operator} {num2} = {res:.2f}")


calculator()



