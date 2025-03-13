import pytest


@pytest.fixture  # Фикстуры для проверки правильного скрытия счета
def acc_number() -> list[tuple[str, str]]:
    return [
        ("73654108430135874305", "**4305"),
        ("12341234123412341234", "**1234"),
        ("99559485465423112458", "**2458"),
        ("45654565458795123548", "**3548"),
        ("55559875456213247999", "**7999"),
    ]


@pytest.fixture  # Фикстуры для проверки вызова ошибок
def acc_number_error() -> tuple:
    return (
        "asdasdasdsaddasdasda",
        "asd",
        "asdsadasdadsadadasdsadasda",
        "ASDASDASDASDASDASDAS",
        "ASD",
        "ASDASDASDASDASDASDASDASD",
    )


@pytest.fixture  # Фикстуры для проверки вызова ошибок
def card_number_error() -> tuple:
    return ("asdfasdfasdfasdf", "ASDFASDFASDFASDF", "asd", "ASD", "asdasdadasdasdasdadas", "ASDFDSADASDSAADSSDADS")


@pytest.fixture  # Фикстуры с для проверки скрытия номера карт
def card_number() -> list[tuple[str, str]]:
    return [
        ("7000792289606361", "7000 79** **** 6361 "),
        ("1234123412341234", "1234 12** **** 1234 "),
        ("1456456879878464", "1456 45** **** 8464 "),
        ("4564545654456456", "4564 54** **** 6456 "),
        ("7894561237894563", "7894 56** **** 4563 "),
    ]


@pytest.fixture  # Фикстуры с разными картами и счетами
def card_or_account() -> list[tuple[str, str]]:
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199 "),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758 "),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658 "),
    ]


@pytest.fixture  # Фикстуры с разными датами
def date() -> list[tuple[str, str]]:
    return [
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ]


@pytest.fixture  # Фикстуры с разными id
def state() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
