# 1. Свойства (@property)
# 1.1. Валидация через setter. Создай класс Product с ценой price.
# Сделай свойство price, которое не позволяет задавать отрицательную цену,
# получать (читать) цену можно.

print("Exercise 1.1")


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price must be greater than 0")

p = Product(100)
print(p.price) # 100
p.price = 250
print(p.price) # 250
p.price = -10 # Отрицательную цену задать нельзя
print(p.price) # 250



# 1.2. Вычисляемое свойство (площадь прямоугольника)
# Задание:
# Создай класс Rectangle с атрибутами width и height.
# Добавь свойство area, которое вычисляется на лету.
# Свойство для чтения и записи width и height не нужно.

print("\nExercise 1.2")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area) # 12
rect.width = 10
print(rect.area)



# 1.3. Свойство для процента выполнения тестов
# Задание:
# Создай класс TestStats с атрибутами экземпляра класса passed и total.
# Добавь свойство success_rate (в процентах, только для чтения).

print("\nExercise 1.3")


class TestStats:
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total

    @property
    def success_rate(self):
        if self.passed == 0:
            return 0.0
        return (self.passed / self.total) * 100

stats = TestStats(8, 10)
print(stats.success_rate) # 80.0
stats.passed = 9
print(stats.success_rate) # 90.0


# 2. Множественное наследование, делегирование
# 2.1. Миксин для проверки прав
# Сделай PermissionMixin с методом has_permission(user_role), который
# возвращает True только для роли "admin".
# Сделай класс SecureAction, который использует миксин и в методе
# execute(role) выполняет действие только если есть права.

print("\nExercise 2.1")


class PermissionMixin:
    def has_permission(self, user_role):
        return True if user_role == "admin" else False


class SecureAction(PermissionMixin):
    def execute(self, role):
        if self.has_permission(role):
            print( "Admin. Method started")
        else:
            print("No rights")


action = SecureAction()
action.execute("user") # Нет прав.
action.execute("admin") # Админ. Метод запущен



# 2.2 Делегирование логгеру
# Сделай класс Logger с методом log(message).
# Сделай класс Service, который содержит внутри Logger и в методе process()
# делегирует ему логирование.
# Метод лог принимает строку и принтит её с припиской “[Log]”.
# Метод process просто принтит “Обработка данных”, но перед и после вызывает логер и
# передает сообщение о начале и конце обработки.

print("\nExercise 2.2")


class Logger:
    def log(self, message):
        print(f"[Log] {message}")


class Service():
    def __init__(self):
        self.logger = Logger()

    def process(self):
        self.logger.log("Start processing")
        print("Data processing")
        self.logger.log("Finish processing")


s = Service()
s.process()



# 2.3. Разные роли пользователя
# Сделай классы Admin и Support:
# ● Admin с методом create_user();
# ● Support с методом create_ticket().
# Создай класс SuperUser, который наследует оба и может делать и то, и другое.

print("\nExercise 2.3")


class Admin:
    def create_user(self, user):
        print(f"User created: {user}")

class Support:
    def create_ticket(self, ticket):
        print(f"Ticket created: {ticket}")

class SuperUser(Admin, Support):
    pass


su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")


# 2.4. Порядок разрешения методов (MRO)
# Сделай классы A, B(A), C(A) и D(B, C).
# В A, B, C определи.переопредели метод who_am_i() который просто печатает А, B,
# C в зависимости от имени класса в котором он определен, выведи D.mro().

print("\nExercise 2.4")

class A:
    def who_am_i(self):
        print("A")

class B(A):
    def who_am_i(self):
        print("B")

class C(A):
    def who_am_i(self):
        print("C")

class D(B, C):
    pass

d = D()
d.who_am_i() # B (по MRO)
print(D.mro())


# 2.5. Несколько миксинов
# Сделай миксины:
# ● LoggingMixin — метод log();
# ● RetryMixin — метод retry() (3 попытки вызова self.run() с выводом номера попытки).
# Сделай Job, который наследует оба и реализует run().

print("\nExercise 2.5")


class LoggingMixin:
    def log(self):
        print("[Log] Completing the task")

class RetryMixin:
    def retry(self, attempts):
        i = 1
        while i <= attempts:
            print(f"Attempt № {i}")
            self.run()
            i += 1


class Job(RetryMixin, LoggingMixin):
    def run(self):
        self.log()
        print("Job started")


j = Job()
j.retry(2)


# 3. Абстракция
# 3.1. Базовый абстрактный класс «Фигура»
# Создать абстрактный класс Shape с абстрактным методом area().
# Реализовать классы Rectangle и Circle, которые считают площадь.

print("\nExercise 3.1.")


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * (self.radius * self.radius), 2)


shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    print(s.area())



# 3.2. Абстракция «Транспорт» с шаблонным методом
# Создать абстрактный класс Transport с абстрактным методом move() и
# конкретным методом go(), который выводит «Начинаем движение» и затем
# вызывает move(). Реализовать Car и Bike.

print("\nExercise 3.2.")


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    def go(self):
        print("Start going")
        self.move()


class Car(Transport):
    def move(self):
        print("Going by car")


class Bike(Transport):
    def move(self):
        print("Going by bike")


for t in (Car(), Bike()):
    t.go()


# 3.3. Абстракция для автотестов: BaseTestCase
# Создать абстрактный класс BaseTestCase с методами prepare_data(), run_test()
# и конкретным run(), который вызывает их по порядку. Реализовать тесты
# LoginTest и PaymentTest.

print("\nExercise 3.3.")


class BaseTestCase(ABC):
    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    def run(self):
        self.prepare_data()
        self.run_test()

class LoginTest(BaseTestCase):
    def prepare_data(self):
        print("Готовим пользователя для логина")

    def run_test(self):
        print("Проверяем успешный логин")


class PaymentTest(BaseTestCase):
    def prepare_data(self):
        print("Готовим данные карты и баланс")

    def run_test(self):
        print("Проверяем успешный платеж")

tests = [LoginTest(), PaymentTest()]
for t in tests:
    t.run()


# 4.Полиморфизм. 4.1. Полиморфные тесты (API и UI)
# Создай базовый класс BaseTest с методом run().
# Создай классы APITest и UITest, которые реализуют run() по‑разному.
# Напиши функцию run_all(tests), которая запускает список тестов, не проверяя их тип.

print("\nExercise 4.1.")


class BaseTest(ABC):
    @abstractmethod
    def run(self):
        pass

class APITest(BaseTest):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def run(self):
        print(f"API test: checking endpoint /{self.endpoint}")

class UITest(BaseTest):
    def __init__(self, page):
        self.page = page

    def run(self):
        print(f"UI test: checking page {self.page}")


def run_all(tests):
    for i in tests:
        i.run()


tests = [APITest("login"), UITest("LoginPage"), APITest("users")]
run_all(tests)


# 4.2. Полиморфизм через утиный тип (без ABC)
# Напиши функцию print_length(obj), которая печатает длину чего угодно, что
# поддерживает len(). Проверь на строке, списке, словаре и своём классе
# TestCollection с реализованным __len__.

print("\nExercise 4.2.")

def print_length(obj):
    print(len(obj))

class TestCollection:
    def __init__(self, tests):
        self.tests = tests
    def __len__(self):
        return len(self.tests)

print_length("Python") #6
print_length([1, 2, 3]) #3
print_length({"a": 1,"b" : 2}) #2
print_length(TestCollection([10, 20, 30, 40])) #4



# 5. Магические методы
# 5.1. Коллекция результатов как словарь (__getitem__, __setitem__, __len__)
# Сделай класс TestResults, который:
# ● хранит результаты тестов по имени;
# ● поддерживает операции:
# ● results["test_login"] = "passed";
# ● results["test_login"];
# ● len(results) — количество сохранённых тестов.
# Такая реализация позволяет использовать свой класс почти как обычный
# словарь.

print("\nExercise 5.1.")


class TestResults:
    def __init__(self):
        self._data = {}

    def __setitem__(self, test_name, status):
        self._data[test_name] = status

    def __getitem__(self, test_name):
        return self._data[test_name]

    def __delitem__(self, test_name):
        del self._data[test_name]

    def __len__(self):
        return len(self._data)

results = TestResults()
results["test_login"] = "passed"
results["test_payment"] = "failed"
print(results["test_login"]) # passed
print(len(results)) # 2


# 5.2. Длительность теста с арифметикой (__add__, __str__)
# Создай класс Duration, который хранит время в секундах и:
# ● поддерживает сложение d1 + d2 (возвращает новый Duration);
# ● при print(d) выводит "X.XX sec".

# Так реализуется перегрузка оператора + для пользовательских типов.

print("\nExercise 5.2.")


class Duration:
    def __init__(self, seconds):
        self.seconds = seconds

    def __str__(self):
        return f"{self.seconds:.2f} sec"

    def __add__(self,other):
        return Duration(self.seconds + other.seconds)


d1 = Duration(1.5)
d2 = Duration(2.7)
d3 = d1 + d2

print(d1) # 1.50 sec
print(d2) # 2.70 sec
print(d3) # 4.20 sec


# 5.3. Объект как функция (__call__) — запуск набора тестов
# Создай класс TestRunner, который:
# ● принимает список имён тестов;
# ● при вызове объекта runner() печатает список и количество тестов.

# __call__ делает экземпляры «вызываемыми», что удобно для обёрток, раннеров
# и конфигураций.​

print("\nExercise 5.3.")

class TestRunner:
    def __init__(self, tests):
        self.tests = tests

    def __call__(self):
        print("Запускаем тесты:")
        for test in self.tests:
            print(f"- {test}")
        print(f"Всего тестов: {len(self.tests)}")

runner = TestRunner(["test_login", "test_signup", "test_payment"])
runner()