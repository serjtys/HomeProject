from typing import Any, Dict

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    transactions: list[Dict],
    usd_transactions_correct: Any,
    rub_transactions_correct: Any,
) -> None:
    """Тест проверяет корректность выполнения по ключу,
    Корректность работы при отсутствии ключа и словаря"""
    usd_transactions = filter_by_currency(transactions, "USD")
    rub_transactions = filter_by_currency(transactions, "RUB")
    for i in range(2):
        assert next(usd_transactions) == usd_transactions_correct[i]
        assert next(rub_transactions) == rub_transactions_correct[i]


def test_transaction_descriptions(transactions: list[Dict], descriptions_correct: Any) -> None:
    """Тест проверяет корректность выполнения функции,
    Корректность работы при пустом словаре"""
    descriptions = transaction_descriptions(transactions)
    for i in range(5):
        assert next(descriptions) == descriptions_correct[i]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            0,
            5,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            500000,
            500005,
            [
                "0000 0000 0050 0000",
                "0000 0000 0050 0001",
                "0000 0000 0050 0002",
                "0000 0000 0050 0003",
                "0000 0000 0050 0004",
                "0000 0000 0050 0005",
            ],
        ),
        (
            9999999999999995,
            10000000000000000,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
                "Конец свободных номеров",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, end: int, expected: Any) -> Any:
    """Тест проверяет корректность генерации данных при разных значения,
    соответствия формата карт и случай, если заканчиваются номера карт"""
    card_num = card_number_generator(start, end)
    for i in range(5):
        assert next(card_num) == expected[i]
