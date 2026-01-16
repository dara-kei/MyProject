# Во вложении есть dummy_test_runner.py файл, который имитирует запуск тестов.
# Доработайте файл так, чтоб из него можно было собрать некий отчет (сколько тестов
# всего, сколько прошло, сколько упало, сообщение об ошибке, процент прошедших и то
# что вы еще придумаете). Соберите эти данные в удобный JSON файл.

def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

failed = 0
passed = 0
errors = []
tests_passed = []
tests_failed = []

i = 0

for result, expected in tests:
    i += 1
    try:
        assert result == expected
        passed += 1
        tests_passed.append(i)
        print("Тест прошёл!")
    except AssertionError as e:
        error = f"Тест №{i} не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}"
        errors.append(error)
        failed += 1
        tests_failed.append(i)
        print(f"Тест №{i} не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}")
        continue


report = {'total' : len(tests),
          'passed' : passed,
          'failed' : failed,
          'percent_passed' : round(passed / len(tests) * 100, 2),
          'tests_passed' : tests_passed,
          'tests_failed' : tests_failed,
          'errors' : errors,
}

print(report)


import json
import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom



with open("my_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f,  indent = 2, ensure_ascii = False)

with open("my_report.yaml", "w", encoding="utf-8") as f2:
    yaml.dump(report, f2, default_flow_style=False, sort_keys=False, allow_unicode=True)


root = ET.Element("my_report")
total_el = ET.SubElement(root, "total")
total_el.text = str(report["total"])

passed_el = ET.SubElement(root, "passed")
passed_el.text = str(report["passed"])

failed_el = ET.SubElement(root, "failed")
failed_el.text = str(report["failed"])

percent_el = ET.SubElement(root, "percent_passed")
percent_el.text = str(report["percent_passed"])

tests_passed_el = ET.SubElement(root, "tests_passed")
for num in report["tests_passed"]:
    t = ET.SubElement(tests_passed_el, "test")
    t.text = str(num)

tests_failed_el = ET.SubElement(root, "tests_failed")
for num in report["tests_failed"]:
    t = ET.SubElement(tests_failed_el, "test")
    t.text = str(num)

errors_el = ET.SubElement(root, "errors")
for err in report["errors"]:
    e = ET.SubElement(errors_el, "error")
    e.text = err

tree = ET.ElementTree(root)
tree.write("my_report.xml", encoding="utf-8", xml_declaration=True)

