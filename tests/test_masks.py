import pytest
from unittest.mock import patch

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("0123", "Введите 20-и значный номер лицевого счета"),
        ("", "Введите 20-и значный номер лицевого счета"),
        ("123456789012345678901", "Введите 20-и значный номер лицевого счета"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361 "),
        ("0123", "Введите 16 цифр номера карты"),
        ("", "Введите 16 цифр номера карты"),
        ("12345678901234567", "Введите 16 цифр номера карты"),
    ],
)
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("invalid_input", ["abc", "ABC", "123abc", "ABC123"])
def test_get_mask_account_invalid_chars(invalid_input):
    with pytest.raises(ValueError, match="Недопустимый символ в номере счета"):
        get_mask_account(invalid_input)


@pytest.mark.parametrize("invalid_input", ["abc", "ABC", "123abc", "ABC123"])
def test_get_mask_card_number_invalid_chars(invalid_input):
    with pytest.raises(ValueError, match="Недопустимый символ в номере карты"):
        get_mask_card_number(invalid_input)


@patch("src.masks.masks_logger")
def test_get_mask_account_logging(mock_logger):
    get_mask_account("73654108430135874305")
    mock_logger.info.assert_called_with("Успех")


@patch("src.masks.masks_logger")
def test_get_mask_card_number_logging(mock_logger):
    get_mask_card_number("7000792289606361")
    mock_logger.info.assert_called_with("Успех")