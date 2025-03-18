import time
from typing import Any, Callable


def log(filename: Any = None) -> Any:
    def my_decorator(func: Callable[..., Any]) -> Any:
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
