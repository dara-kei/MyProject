import datetime


# 1. Получите текущую дату и время и выведите их.

now = datetime.datetime.now()
print(now)


# 2. Создайте объект datetime для даты вашего рождения.

my_birth = datetime.date(1991, 8, 24)
print(my_birth)


# 3. Выведите год, месяц и день текущей даты отдельно.

print(now.year)
print(now.month)
print(now.day)


# 4. Отформатируйте текущую дату в строку формата ДД-ММ-ГГГГ.

str = now.strftime("%d-%m-%Y")
print(str)


# 5. Преобразуйте строку "31/12/2025 23:59:59" в объект datetime.


d = datetime.datetime.strptime("31/12/2025 23:59:59", "%d/%m/%Y %H:%M:%S")
print(d)


# 6. Создайте дату через 10 дней от текущего момента.

future = now + datetime.timedelta(days=10)
print(future)


# 7. Вычислите разницу в днях между сегодняшним днем и 1 января этого
# года.

diff = datetime.date(2026, 1, 1) - now.date()
print(diff)


# 8. Напишите функцию, которая получает дату и возвращает, является ли она
# выходным днем (суббота или воскресенье).

def define_weekend (date):
    if date.weekday() == 6 or date.weekday() == 7:
        print("It is a weekend")
    else:
        print("It is a weekday")

define_weekend(now)


# 9. Получите текущую дату и время с часовым поясом UTC+3.

utc_plus_3 = datetime.timezone(datetime.timedelta(hours=3))
now_plus_3 = datetime.datetime.now(utc_plus_3)
print(now_plus_3)


# 10. Создайте лямбда-функцию, которая принимает дату и возвращает её год.

get_year = lambda date : date.year
print(get_year(now))



