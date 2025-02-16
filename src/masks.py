def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты, проверяет что бы цифр было меньше 16, скрывает часть
    через пробел выводит скрытый номер"""
    card_number_str = str(card_number)
    if len(card_number_str) < 16:
        return "Введите 16 цифр номера карты"
    else:
        return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]} "


def get_mask_account(personal_account: int) -> str:
    """Функция принимает номер счета, проверяет что бы цифр было меньше 20, скрывает часть
    через пробел выводит скрытый номер"""
    personal_account_str = str(personal_account)
    if 20 < len(personal_account_str):
        return "Введите 20-и значный номер лицевого счета"
    else:
        return f"**{personal_account_str[2:]}"
