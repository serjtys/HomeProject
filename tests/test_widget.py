import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "acc_and_card, mask_number",
    [
        ("Maestro 159", "Введите 16 цифр номера карты"),
        ("Maestro 123412341234123412", "Введите 16 цифр номера карты"),
        ("Счет 1234", "Введите 20-и значный номер лицевого счета"),
        ("", "Введите карту или счет"),
    ],
)
def test_mask_account_card(acc_and_card: str, mask_number: str) -> None:
    """Тест проверки кода при разных данных"""
    assert mask_account_card(acc_and_card) == mask_number


def test_mask_account_card_1(card_or_account: list[tuple[str, str]]) -> None:
    """Тест проверки кода при однотипных вводных данных"""
    for name, name_mask in card_or_account:
        assert mask_account_card(name) == name_mask


# def test_mask_account_card_error() -> None:
#   """Тест проверки на ошибки"""
#  with pytest.raises(ValueError):
#     mask_account_card("Maestro dsada")
# with pytest.raises(ValueError):
#   mask_account_card("Счет asd")
# with pytest.raises(IndexError):
#    mask_account_card(" ")


def test_get_date(date: list[tuple[str, str]]) -> None:
    """Проверка кода на сортировку по времени"""
    for date_format_1, date_format_2 in date:
        assert get_date(date_format_1) == date_format_2


def test_get_date_error() -> None:
    """Тест на ошибки"""
    with pytest.raises(ValueError):
        get_date("12:12:12dsa")
