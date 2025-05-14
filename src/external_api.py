import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
RUB = "RUB"


def convert_amount(transaction):
    """Функция конвертации валюты с использованием API"""
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return transaction
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={RUB}&from={code}&amount={amount}"
            headers = {"apikey": API_KEY}
            payload = {}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            print(status_code)
            result = response.text
            if status_code == 200:
                return result
            else:
                return f"Запрос отклонен. Причина {response.reason}"
    except requests.exceptions.RequestException:
        print("Ошибка, некорректные данные")


if __name__ == "__main__":
    transactions_1 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
