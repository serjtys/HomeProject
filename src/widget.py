from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card: str) -> str:
    """Функция принимает счет или карту, разбивает наименовния от чисел,
    проверяет, если введен счет, то использует функцию из модуля masks для скрытия счета.
    Если нет, то номер карты соответсвенно"""
    account_or_card_list = account_or_card.split()
    if "Счет" in account_or_card_list:
        return f"Счет {get_mask_account(account_or_card_list[1])}"
    elif "Счет" not in account_or_card_list and len(account_or_card_list) <= 2:
        return f"{account_or_card_list[0]} {get_mask_card_number(account_or_card_list[-1])}"
    else:
        card_name = " ".join(account_or_card_list[0:-1])
        return f"{card_name} {get_mask_card_number(account_or_card_list[-1])}"


def get_date(my_date: str) -> str:
    """Функция принимает строку с датой и возвращает в формате ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
