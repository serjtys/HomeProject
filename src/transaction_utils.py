import re
from collections import Counter
from typing import List, Dict, Union


def search_transactions_by_description(
        transactions: List[Dict[str, Union[str, float]]],
        search_string: str
) -> List[Dict[str, Union[str, float]]]:
    """
    Фильтрует транзакции по заданной строке в описании с использованием регулярных выражений.

    Args:
        transactions: Список словарей с транзакциями
        search_string: Строка или регулярное выражение для поиска

    Returns:
        Отфильтрованный список транзакций
    """
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [
            t for t in transactions
            if 'description' in t and pattern.search(t['description'])
        ]
    except re.error:
        return []


def count_transactions_by_categories(
        transactions: List[Dict[str, Union[str, float]]],
        categories: List[str] = None
) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.

    Args:
        transactions: Список транзакций
        categories: Список категорий для подсчета (None - все категории)

    Returns:
        Словарь {категория: количество}
    """
    if not transactions:
        return {}

    descriptions = [t.get('description', '') for t in transactions]
    counts = Counter(descriptions)

    if categories is None:
        return dict(counts)

    return {category: counts.get(category, 0) for category in categories}