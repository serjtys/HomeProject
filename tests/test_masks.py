import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("0123", "Введите 20-и значный номер лицевого счета"),
        ("123123123123455456456789", "Введите 20-и значный номер лицевого счета"),
        ("", "Введите 20-и значный номер лицевого счета"),
    ],
)
def test_get_mask_account(account: str, mask_account: str) -> None:
    """Тест проверки кода, маскировки аккаунта, при разных вводных данных"""
    assert get_mask_account(account) == mask_account


def test_get_mask_account_error(acc_number_error: str) -> None:
    """Тест проверки ошибок, связанных с не правильным вводом данных"""
    for acc_alpha in acc_number_error:
        with pytest.raises(ValueError):
            get_mask_account(acc_alpha)


def test_get_mask_account_1(acc_number: list[tuple[str, str]]) -> None:
    """Тест выполнения кода, маскировки аккаунта, при однотипных данных"""
    for number, expected in acc_number:
        assert get_mask_account(number) == expected


@pytest.mark.parametrize(
    "string, mask_card_number",
    [
        ("7000792289606361", "7000 79** **** 6361 "),
        ("0123", "Введите 16 цифр номера карты"),
        ("79879789797987977", "Введите 16 цифр номера карты"),
        ("", "Введите 16 цифр номера карты"),
    ],
)
def test_get_mask_card_number(string: str, mask_card_number: str) -> None:
    """тест проверки кода, при разных вводных данных"""
    assert get_mask_card_number(string) == mask_card_number


def test_get_mask_card_number_error(card_number_error: str) -> None:
    """Тест проверки ошибок"""
    for card_alpha in card_number_error:
        with pytest.raises(ValueError):
            get_mask_card_number(card_alpha)


def test_get_mask_card_number_1(card_number: list[tuple[str, str]]) -> None:
    """Тест проверки кода, при однотипных вводных данных"""
    for number, expected in card_number:
        assert get_mask_card_number(number) == expected
