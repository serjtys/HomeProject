from src.masks import get_mask_account, get_mask_card_number

card_number = int(input("Введите номер карты: "))
personal_account = int(input("Введите номер счета: "))


print(get_mask_card_number(card_number))
print(get_mask_account(personal_account))
