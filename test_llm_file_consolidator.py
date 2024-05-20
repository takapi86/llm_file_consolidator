import unittest
from llm_file_consolidator import preprocess_text, get_token_count, write_output, process_file
from unittest.mock import mock_open, patch

class TestLlm_FileConsolidatorFunctions(unittest.TestCase):
    def test_preprocess_text(self):
        input_text = "Hello   World"
        expected_output = "Hello World"
        self.assertEqual(preprocess_text(input_text), expected_output)

        input_text_newline = "Hello\nWorld"
        self.assertEqual(preprocess_text(input_text_newline), expected_output)

        input_text_tab = "Hello\tWorld"
        self.assertEqual(preprocess_text(input_text_tab), expected_output)

        input_text_mixed = "Hello \n\t  World"
        self.assertEqual(preprocess_text(input_text_mixed), expected_output)

    def test_get_token_count(self):
        input_text = "Hello"
        expected_output = 1
        self.assertEqual(get_token_count(input_text), expected_output)

        input_text = "Hello World"
        expected_output = 2
        self.assertEqual(get_token_count(input_text), expected_output)

        input_text = "Hello, World!"
        expected_output = 4
        self.assertEqual(get_token_count(input_text), expected_output)

    def test_write_output(self):
        output_file = "dummy_output.txt"
        preprocessed_text = "This is a preprocessed text."
        expected_output = preprocessed_text

        m = mock_open()
        with patch("builtins.open", m):
            write_output(output_file, preprocessed_text)

        m.assert_called_once_with(output_file, "w", encoding="utf-8")

        handle = m()
        handle.write.assert_called_once_with(expected_output)

    def test_process_file(self):
        file_path = "dummy_file.txt"
        file_content = "This is a test file content."

        m = mock_open(read_data=file_content)
        with patch("builtins.open", m):
            result = process_file(file_path)
            self.assertEqual(result, file_content)

        m.assert_called_once_with(file_path, "r", encoding='utf-8', errors='ignore')

if __name__ == '__main__':
    unittest.main()
