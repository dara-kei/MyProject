# Задание 1. Генератор только чётных
# Написать генератор even_numbers(iterable), который принимает итерируемый
# объект и выдаёт только чётные числа.
import string

print("exercise 1")


def even_numbers(iterable):
    i = 0
    while i < len(iterable):
        if iterable[i] % 2 == 0:
            yield iterable[i]
        i += 1


print(list(even_numbers([1, 2, 3, 4, 5, 6]))) # [2, 4, 6]



print("\nexercise 2")

# Задание 2. Фильтрация строк по ключевому слову
# На основе read_lines(path) написать генератор filter_lines(path, keyword),
# который выдаёт только строки, содержащие keyword.


def filter_lines(path, keyword):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                yield line.strip()


for line in filter_lines("log.txt", "ERROR"):
    print(line)



print("\nexercise 3")

# Задание 3. Ленивое соединение двух итерируемых
# Написать генератор chain(iter1, iter2), который последовательно выдаёт
# элементы сначала из iter1, затем из iter2 (аналог itertools.chain, но вручную).
# Дополнительная информация: yield в генераторе может быть сколько угодно,
# при следующем вызове генератор продолжает работать с того yield на котором
# остановился.

def chain(iter1, iter2):
    i = 0
    while i  < len(iter1):
        yield iter1[i]
        yield iter2[i]
        i += 1



print(list(chain([1, 2], [3, 4]))) # [1, 2, 3, 4]


print("\nexercise 4")

# Задание 4. Бесконечный итератор
# Создать генератор counter(start=0), который бесконечно считает: start, start+1, start+2, ...


def counter(start = 0):
    while True:
        yield start
        start += 1


c = counter(10)
print(next(c)) # 10
print(next(c)) # 11
print(next(c)) # 12


print("\nexercise 5")

# Задание 5. Ограничение бесконечного генератора
# Используя counter, написать генератор take(n, iterable), который берёт только
# первые n элементов из любого итератора/генератора.


def take(n, iterable):
    i = 0
    while i < n:
        yield next(iterable)
        i += 1


c = counter(100)
print(list(take(5, c))) # [100, 101, 102, 103, 104]


print("\nexercise 6")

# Задание 6. Замена всех пробелов на запятые
# Дана строка "one two three\tfour".
# Нужно заменить любые последовательности пробельных символов одним символом ",".

import re


a = "one two three\tfour"
res = re.sub("\\s", ",", a)

print(res) # one,two,three,four


print("\nexercise 7")

# Задание 7. Выделить домены из e‑mail адресов
# Дан список:
# emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
# Нужно получить список доменов: ['test.com', 'mail.ru', 'sub.example.org'].

emails = ["a@test.com", "b@mail.ru", "ghjk", "user@sub.example.org"]
domains = []

# for email in emails:
#     domain = re.findall("@(.+)", email)
#     if domain:
#         domains.append(domain[0])
#
#
# print(domains) # ['test.com', 'mail.ru', 'sub.example.org']


for email in emails:
    match = re.search("@(.+)", email)  # возвращает Match объект
    if match:
        print(match)# проверяем, что нашли совпадение
        domains.append(match.group(1))  # group(1) - первая группа захвата

print(domains)

print("\nexercise 8")

# Задание 8. Проверка формата даты
# Написать функцию, которая проверяет, что строка соответствует формату YYYY-MM-DD,
# где год — 4 цифры, месяц и день — по 2 цифры.
# Пример:
# ● "2025-12-23" == True
# ● "25-12-23" == False

def is_valid_date(date):
    return bool(re.search(r"^\d{4}-\d{2}-\d{2}$", date))

assert is_valid_date("2025-12-23")
assert not is_valid_date("25-12-23")


print("\nexercise 9")

# Задание 9. Извлечь код ответа из HTTP‑лога
# Есть строка лога:
# log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
# Нужно извлечь код ответа (200) как строку.

log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
def get_response(log):
   return re.search(r"\s(\d{3})", log).group(1)

print(get_response(log))



print("\nexercise 10")

# Задание 10. Валидация пароля
# Написать функцию, которая проверяет пароль по правилам:
# ● длина минимум 8 символов;
# ● есть хотя бы одна заглавная буква;
# ● есть хотя бы одна цифра.
# Можно использовать одно или несколько регулярных выражений.


def is_strong_password(str):
    if len(str) < 8:
        return False
    letters = re.search(r"[A-Z]", str)
    numbers = re.search(r"[0-9]", str)
    if letters and numbers:
        return True
    else:
        return False


assert is_strong_password("Abcdef12")
assert not is_strong_password("abcdef12")
assert not is_strong_password("Abcdefgh")



print("\nexercise 11")

# Задание 11. Удалить HTML‑теги
# Дана строка "<p>Hello <b>world</b>!</p>"
# Нужно удалить все теги, оставив только текст:"Hello world!".

tag = "<p>Hello <b>world</b>!</p>"
result = re.sub(r"</?\w+>", "", tag)
print(result)




print("\nexercise 12")

# Задание 12. Получить все пары ключ=значение
# Дана строка:
# s = "name=John; age=30; city=London;"
# Нужно получить словарь {"name": "John", "age": "30", "city": "London"}.

s = "name=John; age=30; city=London;"

preresult = re.findall(r"(\w+)=(\w+)", s)
result2 = {}
for key, value in preresult:
    result2[key] = value


print(result2) # {'name': 'John', 'age': '30', 'city': 'London'}


print("\nexercise 13")

# Задание 13. Вытащить номер телефона
# В строке могут быть телефоны формата +7-999-123-45-67 или 8 (999) 123-45-67.
# Нужно написать функцию, которая возвращает все телефоны из строки.


text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77. , +7-999-123-45-67"
def find_phones(any_text):
    return re.findall(r"\+\d-\d{3}-\d{3}-\d{2}-\d{2}|\d\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}", any_text)


print(find_phones(text))


print("\nexercise 14")

# Задание 14. Разбить строку по нескольким разделителям
# Разбить "one,two;three four" на слова, используя разделители ,, ; и пробелы.
# Ожидаемый результат: ['one', 'two', 'three', 'four'].


a = "one,two;three four"
print(re.split(r"[,;\s]", a))


print("\nexercise 15")

# Задание 15. Извлечь данные из URL
# Из URL вида /api/v1/users/123/orders/456 извлечь user_id и order_id как  числа.
# Ожидаемый результат: ('123', '456').

url = "/api/v1/users/123/orders/456"
def get_id(text):
    a = re.search(r"users/(\d+)/orders/(\d+)", text)
    if a:
        return a.group(1), a.group(2)

print(get_id(url))
