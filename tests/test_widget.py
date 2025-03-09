from src.widget import mask_account_card, get_date

import pytest

@pytest.mark.parametrize('acc_and_card, mask_number',
                         [
                             ('Maestro 159', 'Введите 16 цифр номера карты'),
                             ('Maestro 123412341234123412', 'Введите 16 цифр номера карты'),
                             ('Счет 1234', 'Введите 20-и значный номер лицевого счета'),
                             ('', 'Введите карту или счет'),
                         ])
def test_mask_account_card(acc_and_card, mask_number):
    assert mask_account_card(acc_and_card) == mask_number

def test_mask_account_card_1(card_or_account):
    for name, name_mask in card_or_account:
        assert mask_account_card(name) == name_mask

def test_mask_account_card_error():
    with pytest.raises(ValueError):
        mask_account_card('Maestro dsada')
    with pytest.raises(ValueError):
        mask_account_card('Счет asd')

def test_get_date(date):
    for date_format_1, date_format_2 in date:
        assert get_date(date_format_1) == date_format_2

def test_get_date_error():
    with pytest.raises(ValueError):
        get_date('12:12:12dsa')
