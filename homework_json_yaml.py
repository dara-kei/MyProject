print("ex.JSON 1.1")

import json


# Сгенерируйте файл test_results.json из python объекта:

results = {
    'test_suite' : 'api_tests',
    'total' : 10,
    'passed' : 8,
    'failed' : 2
}

with open("test_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent = 2)



print("\nex.JSON 1.2")


# Сгенерируйте фаил users.json из python объекта:

data = [
  {
    "id": 1,
    "name": "Sasha",
    "role": "admin"
  }
]

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent = 2)



print("\nex.JSON 1.3")

# Откройте test_results.json файл и посчитайте процент успешно пройденных
# тестов.


with open("test_results.json", "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
        passed = data['passed'] / data['total'] * 100
        print(f'Percentage of tests passed: {passed}')
    except json.JSONDecodeError as e:
        print("Invalid json")



print("\nex.JSON 1.4")

# Откройте users.json файл, добавьте в него своего пользователя и сохраните
# изменения.

my_data = {"id" : 2, "name" : "Daria", "role" : "user"}


with open("users.json", "r", encoding="utf-8") as f:
    old_data = json.load(f)
    old_data.append(my_data)

with open("users.json", "w", encoding="utf-8") as f2:
    json.dump(old_data, f2, indent=2)


print("\nex.JSON 1.5")



import yaml


print("\nex.YAML 2.1")

# 2.1. Сгенерируйте файл test_results.yaml из python объекта:


results = {"test_suite": "api_tests", "total": 10, "passed": 8, "failed": 2}

with open("test_results.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(results, f, default_flow_style = False, sort_keys = False)



print("\nex.YAML 2.2")

# 2.2. Сгенерируйте файл users.yaml из python объекта:

results = [{"id": 1, "name": "Sasha", "role": "admin"}]

with open("users.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(results, f, default_flow_style = False, sort_keys = False)


print("\nex.YAML 2.3")

# 2.3. Откройте test_results.yaml файл и посчитайте процент успешно пройденных тестов.

with open("test_results.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(f'Percentage of tests passed: {data['passed'] / data['total'] * 100}')



print("\nex.YAML 2.4")

# 2.4. Откройте users.yaml файл, добавьте в него своего пользователя и сохраните изменения.


with open("users.yaml", "r") as f:
    data = yaml.safe_load(f)
    data.append(my_data)

with open("users.yaml", "w") as f:
    yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)










