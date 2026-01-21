import logging


def setup_log():
    logging.basicConfig(
        level=logging.DEBUG,
        filename="menu.log",
        filemode="a",
        format="%(asctime)s | %(levelname)s | %(message)s"
    )