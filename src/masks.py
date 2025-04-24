import string
from typing import Union

from src.logger import masks_logger


def get_mask_card_number(card_number: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер карты, проверяет что бы цифр было меньше 16, скрывает часть
    через пробел выводит скрытый номер"""
    card_number_str = str(card_number)

    # Проверка на буквы в номере карты
    if any(c in string.ascii_letters for c in card_number_str):
        masks_logger.error("Недопустимый символ в номере карты")
        raise ValueError("Недопустимый символ в номере карты")

    # Проверка длины номера карты
    if len(card_number_str) != 16:
        masks_logger.warning("Неправильная длина номера карты")
        return "Введите 16 цифр номера карты"

    masks_logger.info("Успех")
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]} "


def get_mask_account(personal_account: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер счета, проверяет что бы цифр было меньше 20, скрывает часть
    через пробел выводит скрытый номер"""
    personal_account_str = str(personal_account)

    # Проверка на буквы в номере счета
    if any(c in string.ascii_letters for c in personal_account_str):
        masks_logger.error("Недопустимый символ в номере счета")
        raise ValueError("Недопустимый символ в номере счета")

    # Проверка длины номера счета
    if len(personal_account_str) != 20:
        masks_logger.warning("Неправильная длина номера счета")
        return "Введите 20-и значный номер лицевого счета"

    masks_logger.info("Успех")
    return f"**{personal_account_str[-4:]}"


# print(get_mask_account("asddasasd"))
