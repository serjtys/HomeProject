
def filter_by_currency(transactions, currency):
    if transactions == [] or currency == '':
        yield 'нет данных'
    else:
        for transaction in transactions:
            if transaction['operationAmount']['currency']['code'] == currency:
                yield transaction
        else:
            for transaction in transactions:
                if transaction['operationAmount']['currency']['code'] != currency:
                    yield 'нет данных'


def transaction_descriptions(transactions):
        for transaction in transactions:
            yield transaction['description']
        else:
            yield 'нет данных'


def card_number_generator(start, end):
    for i in range(start, end + 1):
        count_0 = "0" * (16 - len(str(i)))
        number = count_0 + str(i)
        number_format = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        if len(str(number)) > 16:
            yield 'Конец свободных номеров'
        else:
            yield number_format

#print(list(card_number_generator(9999999999999995, 10000000000000002)))