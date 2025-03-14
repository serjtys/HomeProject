import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(transactions, usd_transactions_correct, rub_transactions_correct):
    usd_transactions = filter_by_currency(transactions, "USD")
    rub_transactions = filter_by_currency(transactions, "RUB")
    for i in range(3):
        assert next(usd_transactions) == usd_transactions_correct[i]
        assert next(rub_transactions) == rub_transactions_correct[i]
    assert list(filter_by_currency([], '')) == ['нет данных']
    assert list(filter_by_currency([], 'RUB')) == ['нет данных']
    assert list(filter_by_currency(['ABC'], '')) == ['нет данных']


def test_transaction_descriptions(transactions, descriptions_correct):
    descriptions = transaction_descriptions(transactions)
    for i in range(5):
        assert next(descriptions) == descriptions_correct[i]
    assert list(transaction_descriptions([])) == ['нет данных']

@pytest.mark.parametrize('start, end, expected',
                         [
                             (0, 5,
                              [
                                  '0000 0000 0000 0000',
                                  '0000 0000 0000 0001',
                                  '0000 0000 0000 0002',
                                  '0000 0000 0000 0003',
                                  '0000 0000 0000 0004',
                                  '0000 0000 0000 0005'
                              ]
                              ),
                             (500000, 500005,
                              [
                                  '0000 0000 0050 0000',
                                  '0000 0000 0050 0001',
                                  '0000 0000 0050 0002',
                                  '0000 0000 0050 0003',
                                  '0000 0000 0050 0004',
                                  '0000 0000 0050 0005'
                              ]
                              ),
                             (9999999999999995, 10000000000000000,
                             [
                                 '9999 9999 9999 9995',
                                 '9999 9999 9999 9996',
                                 '9999 9999 9999 9997',
                                 '9999 9999 9999 9998',
                                 '9999 9999 9999 9999',
                                 'Конец свободных номеров'
                             ]
                             )
                         ]
                            )
def test_card_number_generator(start, end, expected):
    card_num = card_number_generator(start, end)
    for i in range(5):
        assert next(card_num) == expected[i]
