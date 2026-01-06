import math

#     1. Вычислите площадь круга с радиусом 7 (используйте math.pi и pow()).

def sq_circle(radius):
    return math.pow(radius, 2) * math.pi
print(sq_circle(7))

#     2. Найдите наибольшее целое число, не превышающее число 9.8 (используйте math.floor()).

print(math.floor(9.8))

#     7. Найдите факториал числа 8.
print(math.factorial(8))

#     8. Определите степень, в которую нужно возвести 2, чтобы получить 256 (используйте math.log()).
print(math.log(256, 2))

#     9. Округлите число 3.14159 до ближайшего целого с помощью math.ceil().

print(math.ceil(3.14159))


#     10. Напишите функцию, которая принимает угол в градусах и возвращает тангенс этого угла.

def my_tan(degrees):
    radians = math.radians(degrees)
    return math.tan(radians)
print(my_tan(3))