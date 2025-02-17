from .masks import get_mask_account, get_mask_card_number

from datetime import datetime


def mask_account_card(personal_account_or_card_number: str) -> str:
    ''' Функция принимает счет или карту, разбивает наименовния от чисел,
    проверяет, если введен счет, то использует функцию из модуля masks для скрытия счета.
    Если нет, то номер карты соответсвенно '''
    get_personal_account_or_card_number = personal_account_or_card_number.split()
    if "Счет" in get_personal_account_or_card_number:
        return f"Счет {get_mask_account(get_personal_account_or_card_number[1])}"
    elif "Счет" not in get_personal_account_or_card_number and len(get_personal_account_or_card_number) <= 2:
        return f"{get_personal_account_or_card_number[0]} {get_mask_card_number(get_personal_account_or_card_number[-1])}"
    else:
        card_name = " ".join(get_personal_account_or_card_number[0:-1])
        return f"{card_name} {get_mask_card_number(get_personal_account_or_card_number[-1])}"


def get_date(my_date: str) -> str:
    '''Функция принимает строку с датой и возвращает в формате ДД.ММ.ГГГГ'''
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
