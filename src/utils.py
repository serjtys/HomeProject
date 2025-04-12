import json
import os


def load_transactions(file_path):
    if not os.path.isfile(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            transactions = json.load(file)
            if isinstance(transactions, list):
                return transactions
        except json.JSONDecodeError:
            return []
    return []


#  print(load_transactions('../data/operations.json'))
