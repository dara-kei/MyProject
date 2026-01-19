import logging

# базовая настройка (один раз в начале программы)

# Задание 1. Базовое логирование
# Условие. Настроить простое логирование с выводом в консоль.


# logging.basicConfig(
#     level = logging.INFO, # минимум INFO
#     format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
#     datefmt = '%Y-%m-%d  %H:%M:%S'
# )
#
# logging.info("Tests run")
# logging.error("Test login_test fail")
# logging.debug(f"Debug")


# Задание 2. Логирование в файл
# Условие. Все логи писать в test_results.log.

# logging.basicConfig(level = logging.INFO, filename = "my_logs.log", filemode = "w")
#
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")


# Задание 3. Разные уровни для консоли и файла
# Условие. DEBUG в файл, INFO+ в консоль.

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter(
#     '%(asctime)s | %(levelname)s | %(message)s'
# )
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(formatter)
#
# file_handler = logging.FileHandler("app.log", encoding="utf-8")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
#
#
# logger.debug("Только в файл")
# logger.info("В консоль и файл")


# Задание 4. Логирование параметров теста
# Условие. Залогировать URL и ожидаемый статус.

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
#
# url = "https://api.example.com/users"
# expected_status = 200
#
# logging.info(f"Tested URL: {url}")
# logging.info(f"Expected HTTP status: {expected_status}")



# Задание 5. Логирование исключения
# Условие. Обработать ошибку HTTP с полным traceback.

import requests

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    response = requests.get("http://bad-url")
    response.raise_for_status() # вызовет exception с типом - requests.RequestException
except requests.RequestException:
    logging.exception("Error in running HTTP request")

