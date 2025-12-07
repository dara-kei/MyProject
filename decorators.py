# Создать декоратор, который проверяет, что первый аргумент функции положительный
# from os import times_result

print("Practice 1\n")

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


# Декоратор с аргументом
# Написать декоратор @tag(tag_name), который выводит строку с тегом до вызова функции
print("\n Practice 2\n")


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



# 1. Декоратор повторного запуска теста
# Задание: @retry(times=3) — повторяет тест заданное количество раз при
# неудаче. Допишите декоратор.
print("\n Exercise 1\n")


import time
def retry(times):
    def retry_decorator(func):
        def wrapper():
            counter = 1
            while counter <= times:
                res  = func()
                if res == "PASSED":
                    return "Success"
                print(f"Не успешно! попытка номер: {counter}")
                counter += 1
            return"Попыток больше нет"
        return wrapper
    return retry_decorator


@retry(times  = 2)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())



# 2. Декоратор проверки прав доступа
# Задание: @require_role('admin') — проверяет роль пользователя перед
# выполнением теста. В admin_test передадим пользователя и выполним тест
# только в случае если пользователь имеет подходящую роль, в противном случае
# выведем ошибку. Допишите декоратор.

print("\n Exercise 2\n")


def require_role(dec_arg):
    def require_role_decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if arg == dec_arg:
                return func(arg)
            else:
                return f'Ошибка: Требуется роль {dec_arg}, текущая: {arg}'
        return wrapper
    return require_role_decorator


user_one = 'user'
user_two = 'admin'


@require_role("admin")
def admin_test(arg):
    print("Выполняется админский тест")
    return "SUCCESS"


print(admin_test(user_one))



# 3. Декоратор замера времени выполнения
# Задание: Реализуйте декоратор @timer, который измеряет время выполнения теста.
# Текущее время можно узнать добавив “import time” выполнив “time.time()”.
# Имя функции(объекта) можно получить так “func.__name__”

print("\n Exercise 3\n")


def timer(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        res_func = func()
        end_time = time.time()
        result_time = end_time - start_time
        print(f'{func.__name__} executed in {result_time:.2f} seconds')
        return res_func
    return wrapper


@timer
def slow_test():
    time.sleep(1)
    return "OK"

print(slow_test())



# 4. Декоратор ожидания с таймаутом
# Задание: @wait_with_retry_until(timeout=10, interval=0.5) — ждет
# выполнения условия с таймаутом. Чтобы выжидать интервал можно
# воспользоваться “time.sleep(interval)”. Допишите декоратор.

print("\n Exercise 4\n")


def wait_with_retry_until(timeout, interval):
    def real_dec(func):
        @functools.wraps(func)
        def wrapper():
            start_time = time.time()
            counter = 1

            while time.time() - start_time <= timeout:
                res = func()
                if res:
                    print(f'Attempt {counter}: successful')
                    return "Item found"
                print(f'Attempt {counter}: unsuccessful')
                counter += 1
                time.sleep(interval)
            return "Timeout is over"
        return wrapper
    return real_dec



@wait_with_retry_until(timeout = 3, interval = 0.5)
def element_visible():
    return time.time() % 3 > 2 # имитация появления элемента

print(element_visible())


# 5. Декоратор кэширования результатов.
# Задание: @cache_results — кэширует результаты функции по аргументам.
# Дополнительно. Добавьте декоратор @count_exec_time с замером времени
# выполнения к декоратору кэширования(Задание 5).

print("\n Exercise 5\n")


def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(arg):
        if arg in cache:
            return cache[arg]
        else:
            res = func(arg)
            cache[arg] = res
            return res
    return wrapper

def count_exec_time(func):
    @functools.wraps(func)
    def wrapper(arg):
        print(f'{func.__name__} with arg {arg} is running')
        start_time = time.time()
        res = func(arg)
        end_time = time.time()
        print(f'{func.__name__} executed in {end_time - start_time:.6f} seconds')
        return res
    return wrapper


@count_exec_time
@cache_results
def expensive_calculation(n):
    print(f'Calculating with {n}')
    time.sleep(1)
    return n * n

print(expensive_calculation(5)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(6)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша

