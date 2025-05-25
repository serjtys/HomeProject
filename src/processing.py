from typing import Union


def filter_by_state(transactions, state="EXECUTED"):
    """
    Фильтрует транзакции по статусу.
    Автоматически пропускает транзакции без поля 'state'.
    """
    if not transactions:
        return []

    filtered_transactions = []
    for transaction in transactions:
        # Пропускаем транзакции без поля 'state'
        if "state" not in transaction:
            continue

        # Сравниваем статусы, приведя оба к верхнему регистру
        if str(transaction["state"]).upper() == state.upper():
            filtered_transactions.append(transaction)

    return filtered_transactions


def sort_by_date(
    transactions: list[dict[str, Union[str | int]]], reverse: bool = True
) -> list[dict[str, Union[str | int]]]:
    """Функция сортирует списки по времени"""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
