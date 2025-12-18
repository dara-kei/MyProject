# 1. Транспорт
# Задание: Класс Vehicle с атрибутом speed и методом move().
# Класс Car наследует Vehicle и добавляет метод honk().

print('exercise 1\n')


class Vehicle:
    def __init__(self,speed):
        self.speed = speed

    def move(self):
        return f'It is moving with the speed {self.speed}'


class Car(Vehicle):
    def honk(self):
        return f'It is honking: Beep!Beep!'


jaguar = Car(250)
print(jaguar.move())
print(jaguar.honk())

# 2. Сотрудники
# Задание: Класс Employee с атрибутом name, salary.
# Классы Manager и Developer, наследующие Employee с разными зарплатами по умолчанию.

print('\nexercise 2\n')

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self,name,salary = 4000):
        super().__init__(name,salary)


class Manager(Employee):
    def __init__(self,name,salary = 8000):
        super().__init__(name,salary)


maks = Manager('Maks')
tom = Developer('Tom')


print(maks.salary)
print(tom.salary)



# 3. Фигуры
# Задание: Класс Shape с методом area().
# Классы Rectangle и Circle с конкретными реализациями.

print('\nexercise 3\n')


import math


class Shape:
    def area(self):
        return 'Area is '


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return super().area() + str(self.length * self.width)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return super().area() + str(math.pi * (self.radius ** 2))


rectangle = Rectangle(10,20)
print(rectangle.area())
circle = Circle(5)
print(circle.area())



# 4. Банк
# Задание: Класс Account с балансом и методами deposit(), withdraw().
# Класс SavingsAccount наследник, который умеет добавлять процент на баланс (кешбек).

print('\nexercise 4\n')

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return f"Your balance is {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid value")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid value")
        elif amount > self.balance:
            print(f"You don't have enough money to withdraw {amount}")
        else:
            self.balance -= amount


class SavingsAccount(Account):
    def __init__(self,balance, interest = 5):
        super().__init__(balance)
        self.interest = interest
    def add_interest(self):
        this_interest = self.balance * self.interest / 100
        self.balance += this_interest


account = SavingsAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.add_interest()
print(account.get_balance())
account.withdraw(2000)
print(account.get_balance())

