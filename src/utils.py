import json
import os

from src.logger import utils_logger


def load_transactions(file_path):
    """Функция чтения json файлов, принимает в качестве аргумента пусть к файлу"""
    if not os.path.isfile(file_path):
        utils_logger.warning("Файл не найден: %s", file_path)
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            transactions = json.load(file)
            if isinstance(transactions, list):
                utils_logger.info("Успешно загружены транзакции из файла: %s", file_path)
                return transactions
        except json.JSONDecodeError:
            utils_logger.error("Ошибка при декодировании JSON из файла: %s", file_path)
            return []

    return []


print(load_transactions("../data/operations.json"))
