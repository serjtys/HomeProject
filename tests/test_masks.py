from sys import exc_info

from src.masks import get_mask_account, get_mask_card_number

import pytest

@pytest.mark.parametrize('account, mask_account',
                         [
                             ('73654108430135874305', '**4305'),
                             ('0123', 'Введите 20-и значный номер лицевого счета'),
                             ('123123123123455456456789', 'Введите 20-и значный номер лицевого счета'),
                             ('', 'Введите 20-и значный номер лицевого счета'),
                         ])
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account

def test_get_mask_account_error(acc_number_error):
    for acc_alpha in acc_number_error:
        with pytest.raises(ValueError):
            get_mask_account(acc_alpha)

def test_get_mask_account_1(acc_number):
    for number, expected in acc_number:
        assert  get_mask_account(number) == expected


@pytest.mark.parametrize('string, mask_card_number',
                        [
                            ('7000792289606361', '7000 79** **** 6361 '),
                            ('0123', 'Введите 16 цифр номера карты'),
                            ('79879789797987977', 'Введите 16 цифр номера карты'),
                            ('', 'Введите 16 цифр номера карты'),
                        ])
def test_get_mask_card_number(string, mask_card_number):
    assert get_mask_card_number(string) == mask_card_number

def test_get_mask_card_number_error(card_number_error):
    for card_alpha in card_number_error:
        with pytest.raises(ValueError):
            get_mask_card_number(card_alpha)

def test_get_mask_card_number_1(card_number):
    for number, expected in card_number:
        assert get_mask_card_number(number) == expected