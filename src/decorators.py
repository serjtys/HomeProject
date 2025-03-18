import time
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Any:
    """Декоратор, приниает название файла, если он существует, то
    записывает результат в него, если нет, то выводит в консоль
    Результатом является время выполнения функции"""

    def my_decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                print(args)
                result = func(*args, **kwargs)
                message = f"{func.__name__} OK {time.asctime()}"
            except Exception as error:
                result = None
                message = f"{func.__name__} {time.asctime()} error: {error}. Inputs: {args}, {kwargs}"
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(message)
                else:
                    print(message)

            return result

        return inner

    return my_decorator
