import json
import csv
import openpyxl
from typing import List, Dict, Union
from datetime import datetime
from src.transaction_utils import search_transactions_by_description, count_transactions_by_categories
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date


def load_transactions(file_type: str, filename: str) -> List[Dict[str, Union[str, float]]]:
    """Загружает транзакции из файла"""
    try:
        if file_type == "json":
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_type == "csv":
            transactions = []
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    transactions.append(row)
            return transactions
        elif file_type == "xlsx":
            workbook = openpyxl.load_workbook(filename)
            sheet = workbook.active
            headers = [cell.value for cell in sheet[1]]
            return [
                dict(zip(headers, row))
                for row in sheet.iter_rows(min_row=2, values_only=True)
            ]
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return []


def print_transaction(transaction: Dict[str, Union[str, float]]) -> None:
    """Выводит информацию о транзакции"""
    date = get_date(transaction.get('date', ''))
    description = transaction.get('description', '')
    from_acc = mask_account_card(transaction.get('from', '')) if 'from' in transaction else ''
    to_acc = mask_account_card(transaction.get('to', ''))
    amount = transaction.get('operationAmount', {}).get('amount', '')
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('code', '')

    print(f"{date} {description}")
    if from_acc:
        print(f"{from_acc} -> {to_acc}")
    else:
        print(f"{to_acc}")
    print(f"Сумма: {amount} {currency}\n")


def main():
    """Основная логика программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите тип файла для загрузки:")
    print("1. JSON\n2. CSV\n3. XLSX")

    file_type = input("Ваш выбор (1-3): ").strip()
    file_types = {"1": "json", "2": "csv", "3": "xlsx"}

    if file_type not in file_types:
        print("Неверный выбор")
        return

    filename = input("Введите путь к файлу: ").strip()
    transactions = load_transactions(file_types[file_type], filename)

    if not transactions:
        print("Не удалось загрузить транзакции")
        return

    # Фильтрация по статусу
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper().strip()
        if status in {"EXECUTED", "CANCELED", "PENDING"}:
            break
        print("Неверный статус")

    transactions = filter_by_state(transactions, status)

    # Сортировка
    if input("Сортировать по дате? (да/нет): ").lower() == "да":
        reverse = input("По возрастанию или убыванию? ").lower() == "убыванию"
        transactions = sort_by_date(transactions, reverse)

    # Поиск по описанию
    if input("Фильтровать по описанию? (да/нет): ").lower() == "да":
        search_str = input("Введите строку или регулярное выражение: ")
        transactions = search_transactions_by_description(transactions, search_str)

    # Вывод результатов
    print(f"\nНайдено транзакций: {len(transactions)}")
    for t in transactions:
        print_transaction(t)

    # Статистика по категориям
    if transactions:
        print("\nСтатистика по категориям:")
        stats = count_transactions_by_categories(transactions)
        for category, count in stats.items():
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()