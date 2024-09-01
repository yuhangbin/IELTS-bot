import unittest
from unittest.mock import patch, MagicMock
from src.sections import reading

class TestReadingSection(unittest.TestCase):
    @patch('src.sections.reading.IELTSChain')
    @patch('builtins.input', return_value='What is the main idea of the passage?')
    def test_practice(self, mock_input, MockIELTSChain):
        # Arrange
        mock_chain_instance = MockIELTSChain.return_value
        mock_chain_instance.reading_chain.return_value = MagicMock()
        mock_chain_instance.run_chain.return_value = "The main idea of the passage is..."

        # Act
        with patch('builtins.print') as mock_print:
            reading.practice()

        # Assert
        mock_input.assert_called_once_with("Enter your reading question: ")
        mock_chain_instance.reading_chain.assert_called_once()
        mock_chain_instance.run_chain.assert_called_once_with(mock_chain_instance.reading_chain.return_value, 'What is the main idea of the passage?')
        mock_print.assert_any_call("This is the Reading practice section.")
        mock_print.assert_any_call("The main idea of the passage is...")

if __name__ == '__main__':
    unittest.main()
