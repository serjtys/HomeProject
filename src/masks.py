import string
from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер карты, проверяет что бы цифр было меньше 16, скрывает часть
    через пробел выводит скрытый номер"""
    card_number_str = str(card_number)
    for i in string.ascii_lowercase:
        if i in card_number_str:
            raise ValueError
        for i in string.ascii_uppercase:
            if i in card_number_str:
                raise ValueError
            elif len(card_number_str) != 16:
                return "Введите 16 цифр номера карты"
            else:
                return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]} "
    return None


def get_mask_account(personal_account: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер счета, проверяет что бы цифр было меньше 20, скрывает часть
    через пробел выводит скрытый номер"""
    personal_account_str = str(personal_account)
    for i in string.ascii_lowercase:
        if i in personal_account_str:
            raise ValueError
        for i in string.ascii_uppercase:
            if i in personal_account_str:
                raise ValueError
            elif len(personal_account_str) != 20:
                return "Введите 20-и значный номер лицевого счета"
            else:
                return f"**{personal_account_str[-4:]}"
    return None
