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
    if operator == '+':
        return summary(num1, num2)
    elif operator == '-':
        return subtraction(num1, num2)
    elif operator == '*':
        return multiplication(num1, num2)
    elif operator == '/':
        return division(num1, num2)
    elif operator == '**':
        return squaring(num1, num2)
    else:
        raise ValueError("Unknown operator")

