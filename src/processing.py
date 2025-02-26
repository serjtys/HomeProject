from typing import Union

def filter_by_state(transactions: list[dict[str, Union[str | int]]], state = "EXECUTED") -> list[dict[str, Union[str | int]]]:
    state_transactions = []
    for user_info in transactions:
        if user_info["state"] == state:
            state_transactions.append(user_info)
    return state_transactions
