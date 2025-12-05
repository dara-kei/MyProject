# 1. Создать декоратор, который проверяет, что первый аргумент функции положительный
print("1 exercise\n")

def check_positive_arg(func):
    def wrapper(number):
        func(number)
        if number > 0:
            return f'{number} is positive'
        if number < 0:
            return f'{number} is negative'
        else:
            return f'{number} = 0'

    return wrapper

@check_positive_arg
def process_number(num):
     print(f'Processing the number {num}')

print(process_number(8))
print(process_number(-3))
print(process_number(0))


# 2. Декоратор с аргументом
# Написать декоратор @tag(tag_name), который выводит строку с тегом до вызова функции
print("\n2 exercise\n")


import functools
def tag(arg):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper():
            print(f'[{arg}] Function {func.__name__} is running')
            func()
        return wrapper
    return real_decorator

@tag("INFO")
def display():
    print(f"{display.__name__} is running")

display()
