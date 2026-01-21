import argparse


parser = argparse.ArgumentParser(prog = "Calculator", description = "This app does calculations", epilog = "Thank you for reading")
parser.add_argument("num1", type = float, help = "The first number")
parser.add_argument("operator", help = "The operator")
parser.add_argument("num2", type = float,  help = "The second number")
parser.add_argument(
    "--round",
    nargs = "?",
    const = 2,
    default = None,
    type = int,
    help = "Round result if flag used"
)

args = parser.parse_args()


def calculator(num1, operator, num2, rounding):
    if operator not in ["+", "-", "*", "/", "**"]:
        print("Invalid operator")
    elif operator == "/" and num2 == 0:
        print("Division by zero")

    else:
        res = 0

        # Вычисления
        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        elif operator == '/':
            res = num1 / num2
        elif operator == '**':
            res = num1 ** num2

        if rounding is not None:
            print(round(res, rounding))
        else:
            print(res)



calculator(args.num1, args.operator, args.num2, args.round)
