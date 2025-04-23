import unittest
from unittest import TestCase
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
    @patch("os.path.isfile", return_value=True)
    def test_file_exists_and_valid_json(self, mock_isfile, mock_file):
        transactions = load_transactions("fake_path.json")
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["id"], 1)
        self.assertEqual(transactions[1]["amount"], 200)

    @patch("os.path.isfile", return_value=False)
    def test_file_does_not_exist(self, mock_isfile):
        transactions = load_transactions("fake_path.json")
        self.assertEqual(transactions, [])

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json data")
    @patch("os.path.isfile", return_value=True)
    def test_file_exists_but_invalid_json(self, mock_isfile, mock_file):
        transactions = load_transactions("fake_path.json")
        self.assertEqual(transactions, [])

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.isfile", return_value=True)
    def test_file_exists_but_empty_json(self, mock_isfile, mock_file):
        transactions = load_transactions("fake_path.json")
        self.assertEqual(transactions, [])


if __name__ == "__main__":
    unittest.main()
