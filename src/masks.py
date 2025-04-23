import string
from typing import Union
from logger import masks_logger

def get_mask_card_number(card_number: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер карты, проверяет что бы цифр было меньше 16, скрывает часть
    через пробел выводит скрытый номер"""
    card_number_str = str(card_number)
    try:
        for i in string.ascii_lowercase:
            if i in card_number_str:
                masks_logger.error("Недопустимый символ в номере карты")
                raise ValueError
            for i in string.ascii_uppercase:
                if i in card_number_str:
                    masks_logger.error("Недопустимый символ в номере карты")
                    raise ValueError
                elif len(card_number_str) != 16:
                    masks_logger.warning("Неправильная длина номера карты")
                    return "Введите 16 цифр номера карты"
                else:
                    masks_logger.info("Успех")
                    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]} "
        return None
    except ValueError as i:
        masks_logger.exception(("Ошибка при обработке номера карты: %s", i))
    return None

def get_mask_account(personal_account: Union[int, str]) -> Union[None | str]:
    """Функция принимает номер счета, проверяет что бы цифр было меньше 20, скрывает часть
    через пробел выводит скрытый номер"""
    personal_account_str = str(personal_account)
    try:
        for i in string.ascii_lowercase:
            if i in personal_account_str:
                masks_logger.error("Недопустимый символ в номере счета")
                raise ValueError
            for i in string.ascii_uppercase:
                if i in personal_account_str:
                    masks_logger.error("Недопустимый символ в номере счета")
                    raise ValueError
                elif len(personal_account_str) != 20:
                    masks_logger.warning("Неправильная длина номера счета")
                    return "Введите 20-и значный номер лицевого счета"
                else:
                    masks_logger.info("Успех")
                    return f"**{personal_account_str[-4:]}"
        return None
    except ValueError as i:
        masks_logger.exception(("Ошибка при обработке номера счета: %s", i))
    return None

print(get_mask_account("asddasasd"))