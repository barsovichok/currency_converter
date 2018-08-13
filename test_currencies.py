import unittest
import currencies 

class TestCurrencies(unittest.TestCase):

    def test_type(self):
        n = currencies.filter_strange_data('5')
        self.assertEqual(type(n), float)

    def test_wrong_type(self):
        n = currencies.filter_strange_data('%')
        self.assertEqual(n, None)

    def test_letter_type(self):
        n = currencies.filter_strange_data('asdasd')
        self.assertEqual(n, None)

    def test_replace_comma(self):
        n = currencies.filter_strange_data('4,4564')
        self.assertEqual(n, 4.4564)

    def test_replace_space(self):
        n = currencies.filter_strange_data('45 64')
        self.assertEqual(n, 4564)

    def test_get_url(self):
        with self.assertRaises(TypeError):
            currencies.get_daily_currencies()

    def test_get_url_response(self):
        result= currencies.get_daily_currencies('https://www.cbr-xml-daily.ru/daily_json.js')
        self.assertEqual(type(result), float)
        # TypeError:
        # self.assertEqual(n, 4564)

    # def test_negative_value(self):
    #     with self.assertRaises(ValueError):
    #         factorial.factorial_n(-1)

        
if __name__ == '__main__':
    unittest.main()