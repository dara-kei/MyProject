class Car:
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed
    def drive(self):
        print(f'{self.make} is driving')
    def accelerate(self):
        self.speed += 10


jaguar = Car('Jaguar', 250)
print(jaguar.speed)
jaguar.accelerate()
print(jaguar.speed)


class Student:
    total_students = 0
    def __init__(self, name, lastname, level):
        self.name = name
        self.lastname = lastname
        self.level = level
        Student.total_students += 1
    def study(self):
        self.level += 1


mary = Student('Mary', 'Smith', 6)
kate = Student('Kate', 'Smith', 5)
print(f'All students: {Student.total_students}')
print(kate.level)
kate.study()
print(kate.level)

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def is_square(self):
        if self.width == self.height:
            return f'It is a square.'
        else:
            return f'It is a rectangle.'

my_rectangle = Rectangle(100, 200)
print(my_rectangle.area())
print(my_rectangle.is_square())

class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    def info(self):
        print(f'{self.name} {self.author} has {self.pages} pages')

    def read(self):
        print(f'{self.name} is being read')

mybook = Book('The flower', 'Kate Smith', 123)
print(mybook.info())




class Calculator():
    counter = 0
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        Calculator.counter += 1


    def add(self):
        return self.num1 + self.num2
    def substract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

my_num = Calculator(10,12)
print(my_num.add())
print(my_num.substract())
print(my_num.multiply())
print(my_num.divide())

class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} is speaking: '

class Dog(Animal):
    def speak(self):
        return super().speak() + "woof-woof"

class Cat(Animal):
    def speak(self):
        return super().speak() + "miau-miau"

bob = Dog('bob')
print(bob.speak())
kat = Cat('kat')
print(kat.speak())