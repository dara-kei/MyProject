print("Exercise 2")

with open("numbers.txt", "w", encoding="utf-8") as f:
    for i in range(1,6):
        f.write(str(i))
        if i != 5:
            f.write("\n")

with open("numbers.txt", "r", encoding="utf-8") as f:
    print(f.read())



print("\nExercise 3")

def count_lines(file):
    with open(file, "r", encoding="utf-8") as f:
        return len(f.readlines())

print(count_lines("numbers.txt"))



print("\nExercise 4")

with open("numbers2.txt", "w", encoding="utf-8") as f:
    with open("numbers.txt", "r", encoding="utf-8") as f2:
        for line in f2:
            f.write(line)

with open("numbers2.txt", "r", encoding="utf-8") as f2:
    print(f2.read())


print("\nExercise 5")

# Добавить запись в лог
# Реализовать функцию log_message(path, message), которая добавляет строку
# <message>\n в конец файла лога.

def log_message(path, message):
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    return path


log_message("app.log", "Test started")
log_message("app.log", "Test finished")


print("\nExercise 6")

# Прочитать первые N символов
# Написать функцию read_first_chars(path, n), которая возвращает первые n
# символов файла (если меньше — весь файл).

def read_first_chars(path, n):
    with open(path, "r", encoding="utf-8") as f:
        return f.read(n)


print(read_first_chars("log.txt", 6))



print("\nExercise 7")

# Фильтрация строк по ключевому слову
# Написать функцию filter_file(src, dst, keyword), которая читает src и
# записывает в dst только те строки, где есть keyword.

def filter_file(src, dst, keyword):
   with open(src, "r", encoding="utf-8") as f, \
        open(dst, "w", encoding="utf-8") as f2:
           for line in f:
               if keyword in line:
                   f2.write(line)
   return dst


filter_file("log.txt", "errors.txt", "ERROR")



print("\nExercise 8")

# Подсчитать сумму чисел в файле
# В файле nums.txt на каждой строке одно целое число. Написать функцию,
# которая возвращает их сумму.

def sum_file(path):
    with open(path, "r", encoding="utf-8") as f:
        this_sum = 0
        for line in f:
            this_sum += int(line)
        return this_sum

print(sum_file("numbers.txt"))

assert sum_file("numbers.txt") == 1 + 2 + 3 + 4 + 5



print("\nExercise 9")

# Сделать копию бинарного файла (например image.png → image_copy.png) через
# чтение/запись в бинарном режиме.

def copy_binary(path, path2):
    with open(path, "rb") as f:
        with open(path2, "wb") as f2:
            f2.write(f.read())


copy_binary("tim.png", "tim_copy.png")


print("\nExercise 10")

# Безопасное чтение конфигурации
# Файл config.txt содержит строки вида key=value. Написать функцию, которая
# читает файл и возвращает словарь настроек, игнорируя пустые строки и строки, начинающиеся с #.


def read_config(path):
    dir_settings = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) > 0 and line[0] != "#":
                key, value = line.split("=")
                dir_settings[key] = value
    return dir_settings

# # Пример config.txt:
# # host=localhost
# # port=8080
# #
print(read_config("config.txt")) #{"host": "localhost", "port": "8080"}

