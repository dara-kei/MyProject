# 1. Декоратор, добавляющий метаданные тесту
# Создай декоратор test_info(author, component), который добавляет к классу
# атрибуты author и component.

print("Exercise 1")


def test_info(author, component):
    def wrapper(cls):
        cls.author = author
        cls.component = component
        return cls
    return wrapper

@test_info(author="Ivan", component="Auth")
class TestLogin:
    pass

print(TestLogin.author) # Иван
print(TestLogin.component) # Auth



# 2. Декоратор‑регистратор Page Object’ов
# Сделай глобальный пустой список PAGES.
# Декоратор register_page должен добавлять каждую декорированную страницу в
# этот список. Страницы должны быть классами декорированными register_page.

print("\nExercise 2")


PAGES = []

def register_page(cls):
    PAGES.append(cls)
    return cls

@register_page
class LoginPage:
    pass

@register_page
class DashboardPage:
    pass


print([cls.__name__ for cls in PAGES])



# 3. Class-based декоратор для добавления тэга
# Реализуй класс‑декоратор Tag(tag_name), который добавляет атрибут tag ко
# всем декорируемым классам (SmokeTests, RegressionTests).
# Вспомогательная информация:
# print(SmokeTests.tag) # smoke
# print(RegressionTests.tag) # regression

print("\nExercise 3")


class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name
    def __call__(self, cls):
        cls.tag = self.tag_name
        return cls

@Tag("smoke")
class SmokeTests:
    pass

@Tag("regression")
class RegressionTests:
    pass

print(SmokeTests.tag) # smoke
print(RegressionTests.tag) # regression


# 4. Enum окружений и маппинг на URL
# Создай Enum окружений и функцию get_base_url, возвращающую базовый URL по env.
# Вспомогательная информация:
# Пример как выглядят базовые URL
# Environment.DEV: &quot;https://dev.example.com&quot;,
# Environment.STAGE: &quot;https://stage.example.com&quot;,
# Environment.PROD: &quot;https://prod.example.com&quot;,

print("\nExercise 4")


from enum import Enum

class Environment(Enum):
    DEV = "https://dev.example.com"
    STAGE = "https://stage.example.com"
    PROD = "https://example.com"

def get_base_url(environment):
    return environment.value


print(get_base_url(Environment.DEV)) # https://dev.example.com
print(get_base_url(Environment.PROD)) # https://prod.example.com



# 5. Enum приоритета и сортировка задач
# Создай Enum приоритетов с числовыми значениями и отсортируй задачи.
# Вспомогательная информация (код вместо троеточий):
# from enum import Enum
# class Priority(Enum):
# ...
# tasks = [
# ("Починить тест логина", Priority.HIGH),
# ("Обновить документацию", Priority.LOW),
# ("Настроить CI", Priority.MEDIUM),
# ]
# # Сортировка по значению enum
# tasks_sorted = sorted(tasks, key=lambda ...)
# for name, prio in tasks_sorted:
# print(prio.name, "-", name)

print("\nExercise 5")


class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

tasks = [
("Починить тест логина", Priority.HIGH),
("Обновить документацию", Priority.LOW),
("Настроить CI", Priority.MEDIUM),
]

tasks_sorted = sorted(tasks, key = lambda task : task[1].value)

for name, prio in tasks_sorted:
    print(prio.name, "-", name)



# 6. Enum типов тестов и фильтрация
# Создай Enum типов тестов и функцию фильтрации списка по типу.
# class TestType(Enum):
# ...
# tests = [
# ("test_login_api", TestType.API),
# ("test_login_ui", TestType.UI),
# ("test_sum", TestType.UNIT),
# ("test_profile_api", TestType.API),
# ]
# def filter_tests_by_type(tests, test_type: TestType):


print("\nExercise 6")


class TestType(Enum):
    API = "api"
    UI = "ui"
    UNIT = "unit"

def filter_tests_by_type(tests, test_type: TestType):
    filter_list = []
    for test in tests:
        if test[1] == test_type:
            filter_list.append(test)
    return filter_list


tests = [
("test_login_api", TestType.API),
("test_login_ui", TestType.UI),
("test_sum", TestType.UNIT),
("test_profile_api", TestType.API),
]


print(filter_tests_by_type(tests, TestType.API))
print(filter_tests_by_type(tests, TestType.UI))



# 7. Парсер числа из строки
# Функция parse_int_list(strings), которая:
# ● На вход получает список строк.
# ● Пробует каждую преобразовать в int.
# ● Если элемент не число — пропускает его и печатает предупреждение с указанием значения.

print("\nExercise 7")


def parse_int_list(strings):
    lst = []
    for i in strings:
        try:
            int(i)
        except ValueError:
            print(f"Can't convert {i} to an integer.")
        else:
            lst.append(int(i))
    return lst


raw = ["10", "20", "abc", "30", "4.5", "40"]
nums = parse_int_list(raw)
print(nums) # [10, 20, 30, 40]



# 9. Точка на плоскости
# Создай Point с полями x: float, y: float. Создай несколько точек и выведи их
# на экран.

from dataclasses import dataclass, field
print("\nExercise 9")

@dataclass()
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)
print(p1) # Point(x=1.0, y=2.0)
print(p2) # Point(x=-3.5, y=4.2)


# 10. Товар и общая стоимость
# Создай Product с полями name: str, price: float, quantity: int.
# Добавь метод total() для вычисления общей стоимости price * quantity.
# Вспомогательная информация:
# @dataclass
# class Product:
# ...
# Методы в dataclass описываются как в обычном классе, а генерация служебных
# методов делает класс компактным.​

print("\nExercise 10")

@dataclass
class Product:
    name : str
    price: float
    quantity: int = 1
    def total(self):
        return self.price * self.quantity

p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0)
print(p1, "total:", p1.total()) # 100.0
print(p2, "total:", p2.total()) # 25.0



# 11. Книга и авторы
# Создай Book с полями:
# ● title: str
# ● authors: list[str] (по умолчанию пустой список)
# ● year: int | None = None
# Создай несколько книг, выведи их в формате "Название (год) — автор1,
# автор2";.
# Вспомогательная информация (важно: field(default_factory=...)):
# from typing import List, Optional
# @dataclass
# class Book:
# ...
# authors: List[str] = field(default_factory=list)
# ...

print("\nExercise 11")


from typing import List, Optional

@dataclass
class Book:
    title : str
    authors: List[str] = field(default_factory=list)
    year: int | None = None # поле year может быть либо числом (int), либо None, None по умолчанию
    def formatted(self):
        if len(self.authors) > 0 and self.year is not None:
            str_lst = ", ".join(self.authors)
            return f"{self.title} ({self.year}) - {str_lst}"
        elif self.year is None and len(self.authors) > 0:
            str_lst = ", ".join(self.authors)
            return f"{self.title} - {str_lst}"
        elif self.year is not None:
            return f"{self.title} ({self.year})"
        else:
            return f"{self.title}"

# можно написать без if/elif
# def formatted(self):
#     result = self.title
#
#     if self.year is not None:
#         result += f" ({self.year})"
#
#     if self.authors:
#         result += " — " + ", ".join(self.authors)
#
#     return result

b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга")
b3 = Book("Совместный труд", ["Alice", "Bob"])


for b in (b1, b2, b3):
    print(b.formatted())