# # parser_test.py
import unittest
from src.cdparser.csvconverter import split_line_by_fixed_widths


class MyTest(unittest.TestCase):

     def test_split_line(self):
         line = "abcd efgh 1123"
         offsets = [4, 9, 14]
         expected = ['abcd', 'efgh', '1123']
         self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)
         print('first TC completed')

     def test_split_line_with_empty_value(self):
         line = "abcd efgh 1123   "
         offsets = [4, 9, 14, 17]
         expected = ['abcd', 'efgh', '1123', '_']
         self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)

         line = "abcd efgh    1123"
         offsets = [4, 9, 12, 17]
         expected = ['abcd', 'efgh', '_', '1123']
         self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)


if __name__ == '__main__':
   unittest.main()