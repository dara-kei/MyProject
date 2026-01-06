import random
from random import sample

# Задание 1. Бросок кубика
# Смоделируйте бросок шестигранного кубика и выведите результат.
print("1")

print(random.randint(1,6))


# Задание 2. Случайный пароль из букв
# Сгенерировать строку длиной 8 символов, состоящую из случайных латинских букв (маленьких).
# Подсказка: можно использовать строку "abcdefghijklmnopqrstuvwxyz" и random.choice.
print("\n2")


a = "abcdefghijklmnopqrstuvwxyz"
def create_string():
    b = ""
    for i in range(8):
        b += random.choice(a)
    return b
print(create_string())


# Задание 3. Случайный тест-кейс
# Есть список методов HTTP: ["GET", "POST", "PUT", "DELETE"].
# Напишите функцию, которая случайно выбирает один метод.
print("\n3")


def get_method(lst):
    return random.choice(lst)
print(get_method(["GET", "POST", "PUT", "DELETE"]))


# Задание 4. Случайный порядок тестов
# Перемешайте их в случайном порядке перед запуском.
print("\n4")


tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
random.shuffle(tests)
print(tests)


# Задание 5. Выбор нескольких случайных юзеров для проверки
# Выберите 2 случайных пользователя для проверки.
print("\n5")


users = ["alice", "bob", "carol", "dave", "erin"]
print(sample(users, 2))


# Задание 6. Симуляция флейки-теста
# Напишите функцию run_flaky_test(), которая:
#     • с вероятностью 30% возвращает "FAILED",
#     • с вероятностью 70% — "PASSED".
# Используйте random.random().
print("\n6")


def run_flaky_test():
    if random.random() <= 0.3:
        return "FAILED"
    return "PASSED"
print(run_flaky_test())


# Задание 7. Лотерея из чисел
# Сгенерируйте «лотерейный билет» — 6 уникальных чисел от 1 до 49 включительно.
print("\n7")


numbers = list(range(1, 50))
print(sample(numbers, 6))


# Задание 8. Случайный тестовый набор данных
# Создайте функцию generate_test_data(n), которая:
#     • принимает n,
#     • возвращает список из n целых чисел от 0 до 100,
#     • числа могут повторяться.
print("\n8")


def generate_test_data(n, lst):
    return random.choices(lst, k=n)

print(generate_test_data(6, numbers))
