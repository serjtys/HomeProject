from typing import Union


def filter_by_state(
    transactions: list[dict[str, Union[str | int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str | int]]]:
    """Функция принимает список со всеми транзакциями.
    Возвращает список по ключу state"""
    state_transactions = []
    for user_info in transactions:
        if user_info["state"] == state:
            state_transactions.append(user_info)
    return state_transactions


def sort_by_date(
    transactions: list[dict[str, Union[str | int]]], reverse: bool = True
) -> list[dict[str, Union[str | int]]]:
    """Функция сортирует списки по времени"""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
