import time
from typing import Any

from src.decorators import log


def test_log() -> None:
    """Тесты на работу различных функциях 'обернутые' в декоратор"""

    @log()
    def add_numbers(a: int, b: int) -> int:
        return a + b

    result1 = add_numbers(3, 5)
    assert result1 == 8

    @log("log.txt")
    def sub_numbers(a: int, b: int) -> int:
        return a - b

    result2 = sub_numbers(21, 4)
    assert result2 == 17

    with open("log.txt", "r", encoding="utf-8") as file:
        for line in file:
            assert f"sub_numbers OK {time.asctime()}" in line


def test_decorators_2(capsys: Any) -> None:
    """Тесты на работу различных функциях 'обернутые' в декоратор"""

    @log()
    def hello_world() -> None:
        print("Hello, world!")

    hello_world()
    captured = capsys.readouterr()
    assert captured.out in "Hello, world!" or f"hello_world OK {time.asctime()}"


def test_decorators_3() -> None:
    """Тесты на работу декоратора при ошибке"""

    @log()
    def add_numbers_1(a: int, b: int) -> float:
        return a / b

    add_numbers_1(3, 0)
    assert f"add_numbers_1 {time.asctime()} error: division by zero. Inputs: (3,0)"

    @log("log.txt")
    def sub_numbers_1(a: int, b: int) -> float:
        return a / b

    sub_numbers_1(21, 0)
    assert f"sub_numbers_1 {time.asctime()} error: division by zero. Inputs: (21, 0)"

    with open(r"log.txt", "r", encoding="utf-8") as file:
        for line in file:
            assert f"sub_numbers_1 {time.asctime()} error: division by zero. Inputs: (21, 0)" in line


def test_decorators_4(capsys: Any) -> None:
    """Тесты на работу декоратора при ошибке"""

    @log()
    def add_numbers_2(a: int, b: int) -> float:
        return a / b

    add_numbers_2(21, 0)
    captured = capsys.readouterr()
    assert captured.out in "(21, 0)" or f"add_numbers_2 {time.asctime()} error: division by zero. Inputs: (21, 0)"
