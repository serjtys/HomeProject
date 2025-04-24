# tests/test_finance_data_reader.py
import pytest
from unittest.mock import mock_open, patch, MagicMock
import pandas as pd
from pathlib import Path
import csv
from src.finance_data_reader import read_csv_transactions, read_excel_transactions

# Пути к тестовым файлам (положите их в tests/test_data/)
TEST_CSV = Path("../data/transactions.cvs")
TEST_EXCEL = Path("../data/transactions_excel.xlsx")

# Фикстура для создания временного CSV файла
@pytest.fixture
def temp_csv(tmp_path):
    csv_file = tmp_path / "temp.csv"
    with open(csv_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'amount', 'category'])
        writer.writerow([1, '2023-01-01', 100, 'Food'])
    return csv_file

# Фикстура для создания временного Excel файла
@pytest.fixture
def temp_excel(tmp_path):
    excel_file = tmp_path / "temp.xlsx"
    df = pd.DataFrame({
        'id': [1],
        'date': ['2023-01-01'],
        'amount': [100],
        'category': ['Food']
    })
    df.to_excel(excel_file, index=False)
    return excel_file

# Тесты с реальными файлами (если они есть)
if TEST_CSV.exists():
    def test_read_real_csv():
        """Тест чтения реального CSV файла"""
        result = read_csv_transactions(TEST_CSV)
        assert isinstance(result, list)
        if len(result) > 0:
            assert all(isinstance(item, dict) for item in result)

def test_csv_empty_file(tmp_path):
    """Тест пустого CSV файла"""
    empty_file = tmp_path / "empty.csv"
    empty_file.touch()
    with pytest.raises(ValueError, match="Файл CSV пуст или не содержит заголовков"):
        read_csv_transactions(empty_file)

if TEST_EXCEL.exists():
    def test_read_real_excel():
        """Тест чтения реального Excel файла"""
        result = read_excel_transactions(TEST_EXCEL)
        assert isinstance(result, list)
        if len(result) > 0:
            assert all(isinstance(item, dict) for item in result)

# Тесты с моками
def test_read_csv_transactions_success(temp_csv):
    """Тест успешного чтения CSV"""
    result = read_csv_transactions(temp_csv)
    assert len(result) == 1
    assert result[0]['id'] == '1'
    assert result[0]['category'] == 'Food'

def test_read_excel_transactions_success(temp_excel):
    """Тест успешного чтения Excel"""
    result = read_excel_transactions(temp_excel)
    assert len(result) == 1
    assert result[0]['id'] == 1
    assert result[0]['category'] == 'Food'

def test_csv_file_not_found():
    """Тест отсутствия CSV файла"""
    with pytest.raises(FileNotFoundError):
        read_csv_transactions("nonexistent.csv")

def test_excel_file_not_found():
    """Тест отсутствия Excel файла"""
    with pytest.raises(FileNotFoundError):
        read_excel_transactions("nonexistent.xlsx")

@patch('pandas.read_excel')
def test_excel_read_error(mock_read):
    """Тест ошибки чтения Excel"""
    mock_read.side_effect = Exception("Test error")
    with pytest.raises(ValueError, match="Ошибка чтения Excel файла"):
        read_excel_transactions("test.xlsx")

@patch('builtins.open')
def test_csv_read_error(mock_open):
    """Тест ошибки чтения CSV"""
    mock_open.side_effect = Exception("Test error")
    with pytest.raises(ValueError, match="Ошибка чтения CSV файла"):
        read_csv_transactions("test.csv")

def test_excel_empty_file(tmp_path):
    """Тест пустого Excel файла"""
    empty_file = tmp_path / "empty.xlsx"
    pd.DataFrame().to_excel(empty_file, index=False)
    with pytest.raises(ValueError, match="Excel файл пуст"):
        read_excel_transactions(empty_file)

def test_csv_empty_file(tmp_path):
    """Тест пустого CSV файла"""
    empty_file = tmp_path / "empty.csv"
    empty_file.touch()  # Создаем действительно пустой файл
    with pytest.raises(ValueError, match="Файл CSV пуст или не содержит заголовков"):
        read_csv_transactions(empty_file)