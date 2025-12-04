# 1. Применение проверки к результатам тестов
# Создайте функцию apply_test_check(check_func, test_results), которая применяет
# переданную функцию-проверку ко всем результатам тестов и возвращает количество
# прошедших.

print("1 exercise")

# С помощью def and lambda
def apply_test_check(check_func, test_results):
    count_tests = 0
    for test in test_results:
        if check_func(test):
            count_tests += 1
    return count_tests

test_results = [
    {'status' : 'passed'},
    {'status' : 'failed'},
    {'status' : 'passed'}
]

result = apply_test_check(lambda x : x['status'] == 'passed', test_results)

print(f"Tests passed: {result}")


# С помощью List comprehension
lst = [test for test in test_results if test['status'] == 'passed']
print(f'Tests passed: {len(lst)}')


# 2. Фильтрация логов
# Напишите функцию filter_logs(logs, filter_func), которая фильтрует логи по переданному
# условию (например, только ошибки).

print("2 exercise")


def filter_logs(logs, filter_func):
    return [log for log in logs if filter_func(log)]

logs = [
    {'level' : 'INFO', 'message' : 'Test started'},
    {'level' : 'ERROR', 'message' : 'Login failed'},
    { 'level' : 'ERROR', 'message' : 'Timeout occured'}
]
error_logs = filter_logs(logs, lambda x : x['level'] == 'ERROR')
print("Errors: ", error_logs)


# 3.Трансформация данных тестов (Полноценный пример)
# Создайте функцию transform_tests(tests, transform_func), которая применяет переданную
# функцию ко всем тестам (например, умножает время на 1.1 для учета нагрузки).

print("3 exercise")


def transform_tests(tests, transform_func):
    return [transform_func(test) for test in tests]

tests = [
    {'name' : 'test1', 'duration' : 2.0},
    {'name' : 'test2', 'duration' : 3.0}
]
increased_tests = transform_tests(tests, lambda x : {**x, 'duration' : x['duration'] * 1.1})
print('Тесты с увеличенным временем:', increased_tests)


#4. Произвольные аргументы (*args, **kwargs)
# Генератор отчетов
# Напишите функцию generate_report(title, *test_names, format=''html', **options), которая
# генерирует отчет с переданными тестами в указанном формате.

print("4 exercise")


def generate_report(title, *test_names, format = "html", **options):
    print(f'Отчет: {title}\nФормат: {format}\nТесты: {', '.join(test_names)}\nАвтор: {options['author']}')

generate_report('Daily Report', 'test1', 'test2', 'test3', format = 'pdf', author = 'Tester')