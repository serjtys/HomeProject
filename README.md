# Домашняя работа 

## Описание:

Проект "Банковская система" - это приложение для работы с банковской системы, она умеет скрывать часть номера карт, 
лицевого счета, выводить наименование карты и время транзакции.
Транзакции можно отсортировать по статусу и по времени

## Установка:

### Клонируйте репозиторий:
```
git clone https://github.com/serjtys/HomeProject.git
```

### Перейдите в директорию проекта:
```
cd HomeProject
```

## Использование:

Примеры использования функций:
```
from src.widget import get_date, mask_account_card

from src.processing import filter_by_state, sort_by_date

# Пример использования mask_account
account = "Maestro 1596837868705199"
mask_card = mask_account_card(account)

# Пример использования get_date
date = "2024-03-11T02:26:18.671407"
required_time_format = get_date(date)

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Пример использования transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

# Пример использования card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)
    
# Пример использования decorators.py
* Для вывода только в консоль
@log()
def hello_world() -> None:
    print("Hello, world!")

*Для вывода в текстовый документ
@log('log.txt')
def hello_world() -> None:
    print("Hello, world!")

for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](/README.md).

## Тестирование

Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:

```bash
pytest
```

Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функции `filter_by_currency` и `transaction_descriptions`; генератор `card_number_generator`
- `decorators`: функции `log`.

Покрытие тестами составляет более 80% кода проекта.

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте пул-реквест.