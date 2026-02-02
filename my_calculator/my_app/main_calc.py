from my_calculator.my_app import calc_func


def calculator():
    while True:
        ex = input("Press Enter if you want to continue or q if you want to quit: ")
        if ex.lower() == "q":
            break

        num1 = calc_func.input_num("Enter first number: ")
        num2 = calc_func.input_num("Enter second number: ")
        operator = calc_func.input_operator()

        try:
            res = calc_func.calculate(num1, num2, operator)
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



