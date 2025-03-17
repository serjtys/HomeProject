from typing import Any, Dict, Iterator, Optional


def filter_by_currency(transactions: Any, currency: Any) -> Any:
    """Функция принимает список словарей и принимает на вход код для сортировки,
    после чего выводит нужные словари с нужным ключом, в случае, когда словарь и
    ключ не заданы, а также если закончились словари, функция заканчивается сообщением
    об отсутствии данных"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[Dict[str, Any]]) -> Iterator[Optional[str]]:
    """Функция принимает список словарей, и выводит строку под определенным ключом,
    в случае отсутствия ключа выводит сообщение об отсутствии данных"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Any:
    """Функция-генератор принимает диапазон значений и создает номер карты по очереди
    В случае если значения карт выходит за пределы формата карты, выводит сообщение об
    отсутствии свободных номеров"""
    for i in range(start, end + 1):
        count_0 = "0" * (16 - len(str(i)))
        number = count_0 + str(i)
        number_format = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        if len(str(number)) > 16:
            break
        else:
            yield number_format
