# 1. Создайте лямбда-функцию, которая проверяет, прошел ли тест (status == "passed").
# Используйте её с filter() для получения списка успешных тестов из списка результатов.

print("1 exercise")


test_results = [
    {'name': 'login_test', 'status': 'passed', 'duration': 2.1},
    {'name' : 'payment_test', 'status': 'failed', 'duration': 3.5},
    {'name' : 'logout_test', 'status': 'passed', 'duration': 1.2},
]

# С помощью lambda and filter
filtration = list(filter(lambda x : x['status'] == 'passed', test_results))
lst_of_passed_tests = []
for i in filtration:
    lst_of_passed_tests.append(i['name'])
print(lst_of_passed_tests)

# С помощью List comprehension в одну строку
print([x['name'] for x in test_results if x['status'] == 'passed'])


# 2. Используйте лямбда-функцию с sort() для сортировки списка словарей тестов по ключу "duration"

print("2 exercise")


tests = [
    {'name' : 'complex_test', 'duration' : 5.2},
    {'name' : 'simple_test', 'duration' : 1.1},
    {'name' : 'medium_test', 'duration' : 3.4},
]

tests.sort(key = lambda x : x['duration'])
print(tests)


# 3. Проверка валидности email
# Напишите лямбда-функцию, которая возвращает True, если строка содержит "@" и
# заканчивается на ".com" или ".ru".

print("3 exercise")

emails = ['test@gmail.com', 'invalid-email', 'user@company.ru', 'no@domain']


# С помощью lambda
valid_emails = lambda email : '@' in email and email.endswith('.com') or email.endswith('.ru')
list_of_valid_emails = []
for email in emails:
    if valid_emails(email):
        list_of_valid_emails.append(email)
print(f"Valid emails: {list_of_valid_emails}")


# С помощью List comprehension в одну строку
print([email for email in emails if '@' and '.com' in email or '@' and '.ru' in email])

