import pytest

from src.transaction_utils import count_transactions_by_categories, search_transactions_by_description


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Перевод организации", "amount": 100, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 500, "currency": "USD"},
        {"description": "Перевод с карты на карту", "amount": 200, "currency": "EUR"},
        {"description": "Покупка в магазине", "amount": 50, "currency": "RUB"},
        {"description": "Перевод организации", "amount": 300, "currency": "USD"},
    ]


def test_search_transactions_by_description_basic(sample_transactions):
    result = search_transactions_by_description(sample_transactions, "перевод")
    assert len(result) == 3
    assert all("Перевод" in t["description"] for t in result)


def test_search_transactions_by_description_regex(sample_transactions):
    result = search_transactions_by_description(sample_transactions, r"Перевод\s\w+$")
    assert len(result) == 2


def test_search_transactions_by_description_case_insensitive(sample_transactions):
    result = search_transactions_by_description(sample_transactions, "ПЕРЕВОД")
    assert len(result) == 3


def test_search_transactions_by_description_invalid_regex(sample_transactions):
    result = search_transactions_by_description(sample_transactions, "*invalid)")
    assert len(result) == 0


def test_count_transactions_by_categories_all(sample_transactions):
    result = count_transactions_by_categories(sample_transactions)
    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
        "Покупка в магазине": 1,
    }


def test_count_transactions_by_categories_selected(sample_transactions):
    result = count_transactions_by_categories(sample_transactions, ["Перевод организации", "Несуществующая"])
    assert result == {"Перевод организации": 2, "Несуществующая": 0}


def test_count_transactions_by_categories_empty():
    result = count_transactions_by_categories([])
    assert result == {}
