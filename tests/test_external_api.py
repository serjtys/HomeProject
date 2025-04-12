import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_amount


class TestConvertAmount(unittest.TestCase):

    @patch("requests.get")
    def test_convert_rub_amount(self, mock_get):
        # Тест: Транзакция в рублях, должна возвращать исходный объект транзакции.
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}
        result = convert_amount(transaction)
        self.assertEqual(result, transaction)

    @patch("requests.get")
    def test_convert_usd_to_rub(self, mock_get):
        # Тест: Транзакция в USD, проверка конвертации в RUB.
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "USD"}}}

        # Настраиваем мок для ответа API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"result": 82000}'  # Эмулируем ответ API
        mock_get.return_value = mock_response

        result = convert_amount(transaction)
        self.assertEqual(result, '{"result": 82000}')

    @patch("requests.get")
    def test_api_error_response(self, mock_get):
        # Тест: Проверка обработки ошибки при запросе к API.
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "EUR"}}}

        # Эмулируем ответ с ошибкой
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.reason = "Bad Request"
        mock_get.return_value = mock_response

        result = convert_amount(transaction)
        self.assertEqual(result, "Запрос отклонен. Причина Bad Request")

    @patch("requests.get")
    def test_request_exception(self, mock_get):
        # Тест: Проверка обработки исключения.
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "EUR"}}}

        # Настраиваем мок для поднятия исключения
        mock_get.side_effect = requests.exceptions.RequestException

        result = convert_amount(transaction)
        self.assertIsNone(result)  # Если обработка ошибки не предусмотрена, проверьте, как свой код реагирует


if __name__ == "__main__":
    unittest.main()
