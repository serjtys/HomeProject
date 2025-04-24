import csv

import pandas as pd


def read_csv_transactions(csv_filepath):
    """
    Считывает финансовые операции из CSV-файла.
    В качестве аргумента путь к CSV-файлу.
    Возвращает список словарей с транзакциями.
    """
    try:
        transactions = []
        with open(csv_filepath, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                raise ValueError("Файл CSV пуст или не содержит заголовков")
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        raise
    except ValueError:
        raise
    except Exception as e:
        raise ValueError("Ошибка чтения CSV файла") from e


def read_excel_transactions(excel_filepath):
    """
    Считывает финансовые операции из Excel-файла.
    В качестве аргумента путь к Excel-файлу.
    Возвращает Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(excel_filepath)
        if df.empty:
            raise ValueError("Excel файл пуст")
        return df.to_dict("records")
    except FileNotFoundError:
        raise
    except ValueError:
        raise
    except Exception as e:
        raise ValueError("Ошибка чтения Excel файла") from e


# Пример использования
if __name__ == "__main__":
    csv_file = "../data/transactions.csv"
    excel_file = "../data/transactions_excel.xlsx"

    csv_transactions = read_csv_transactions(csv_file)
    excel_transactions = read_excel_transactions(excel_file)

    print("Транзакции из CSV:", csv_transactions[:1])
    print("Транзакции из Excel:", excel_transactions[:1])
