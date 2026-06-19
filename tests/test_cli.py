import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Добавляем корень проекта в sys.path для импортов
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli import ZeroEyeCLI

class TestZeroEyeCLI(unittest.TestCase):
    def setUp(self):
        self.cli = ZeroEyeCLI()

    @patch('cli.check_prerequisites')
    def test_handle_check_success(self, mock_check):
        mock_check.return_value = []
        self.assertEqual(self.cli.handle_check(), 0)

    @patch('cli.check_prerequisites')
    def test_handle_check_failure(self, mock_check):
        mock_check.return_value = ["Rust (cargo)"]
        self.assertEqual(self.cli.handle_check(), 1)

    def test_handle_list(self):
        # Проверяем, что метод не падает
        try:
            self.cli.handle_list()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

    @patch('cli.build_module')
    def test_handle_build_all_success(self, mock_build):
        mock_build.return_value = (True, 1.0, "Success output")
        # Эмулируем вызов handle_build с аргументами
        args = MagicMock()
        args.module = "all"
        args.release = False
        args.verbose = False
        
        self.assertEqual(self.cli.handle_build(args), 0)
        self.assertEqual(mock_build.call_count, 10) # 10 модулей в списке

    @patch('cli.build_module')
    def test_handle_build_single_success(self, mock_build):
        mock_build.return_value = (True, 1.0, "Success output")
        args = MagicMock()
        args.module = "backend"
        args.release = False
        args.verbose = False
        
        self.assertEqual(self.cli.handle_build(args), 0)
        self.assertEqual(mock_build.call_count, 1)

    def test_handle_clean_all(self):
        with patch('cli.clean_module') as mock_clean:
            args = MagicMock()
            args.module = "all"
            self.assertEqual(self.cli.handle_clean(args), 0)
            self.assertEqual(mock_clean.call_count, 10)

if __name__ == "__main__":
    unittest.main()
