import unittest
import configini


class TestString(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            string_text = configini.get('string', 'text')
            string_integer = configini.get('string', 'integer')
            string_double_quotes = configini.get('string', 'double_quotes')
            string_single_quotes = configini.get('string', 'single_quotes')
            none_no_text = configini.get('string', 'no_text')

        cls.config = Config

    def test_str_text(self):
        self.assertEqual(type(self.config.string_text), str)

    def test_str_integer(self):
        self.assertEqual(type(self.config.string_integer), str)

    def test_str_double_quotes(self):
        self.assertEqual(type(self.config.string_double_quotes), str)

    def test_str_single_quotes(self):
        self.assertEqual(type(self.config.string_single_quotes), str)

    def test_none_no_text(self):
        self.assertIsNone(self.config.none_no_text)


class TestInteger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            zero = configini.get('number', 'zero', data_type=int)
            one = configini.get('number', 'one', data_type=int)
            negative_one = configini.get('number', 'negative_one', data_type=int)
            zero_with_dot = configini.get('number', 'zero_with_dot', data_type=int)
            one_with_dot = configini.get('number', 'one_with_dot', data_type=int)
            negative_one_with_dot = configini.get('number', 'negative_one_with_dot', data_type=int)
            one_dot_five = configini.get('number', 'one_dot_five', data_type=int)

        cls.config = Config

    def test_integer_zero(self):
        self.assertEqual(type(self.config.zero), int)

    def test_integer_one(self):
        self.assertEqual(type(self.config.one), int)

    def test_integer_negative_one(self):
        self.assertEqual(type(self.config.negative_one), int)

    def test_integer_zero_with_dot(self):
        self.assertEqual(type(self.config.zero_with_dot), int)

    def test_integer_one_with_dot(self):
        self.assertEqual(type(self.config.one_with_dot), int)

    def test_integer_negative_one_with_dot(self):
        self.assertEqual(type(self.config.negative_one_with_dot), int)

    def test_integer_one_dot_five(self):
        self.assertEqual(type(self.config.one_dot_five), int)


class TestFloat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            zero = configini.get('number', 'zero', data_type=float)
            one = configini.get('number', 'one', data_type=float)
            negative_one = configini.get('number', 'negative_one', data_type=float)
            zero_with_dot = configini.get('number', 'zero_with_dot', data_type=float)
            one_with_dot = configini.get('number', 'one_with_dot', data_type=float)
            negative_one_with_dot = configini.get('number', 'negative_one_with_dot', data_type=float)
            one_dot_five = configini.get('number', 'one_dot_five', data_type=float)

        cls.config = Config

    def test_integer_zero(self):
        self.assertEqual(type(self.config.zero), float)

    def test_integer_one(self):
        self.assertEqual(type(self.config.one), float)

    def test_integer_negative_one(self):
        self.assertEqual(type(self.config.negative_one), float)

    def test_integer_zero_with_dot(self):
        self.assertEqual(type(self.config.zero_with_dot), float)

    def test_integer_one_with_dot(self):
        self.assertEqual(type(self.config.one_with_dot), float)

    def test_integer_negative_one_with_dot(self):
        self.assertEqual(type(self.config.negative_one_with_dot), float)

    def test_integer_one_dot_five(self):
        self.assertEqual(type(self.config.one_dot_five), float)


class TestBool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            bool_with_1 = configini.get('bool', '1', data_type=bool)
            bool_with_true = configini.get('bool', 'true', data_type=bool)
            bool_with_text = configini.get('bool', 'text', data_type=bool)
            bool_with_0 = configini.get('bool', '0', data_type=bool)
            bool_with_false = configini.get('bool', 'false', data_type=bool)
            bool_none = configini.get('none', 'none', data_type=bool)

        cls.config = Config

    def test_bool_with_1(self):
        self.assertEqual(self.config.bool_with_1, True)

    def test_bool_with_true(self):
        self.assertEqual(self.config.bool_with_true, True)

    def test_bool_with_text(self):
        self.assertEqual(self.config.bool_with_text, True)

    def test_bool_with_0(self):
        self.assertEqual(self.config.bool_with_0, False)

    def test_bool_with_false(self):
        self.assertEqual(self.config.bool_with_false, False)

    def test_bool_none(self):
        self.assertEqual(self.config.bool_none, False)


class TestList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            list_text = configini.get('list', 'text', data_type=list)
            list_number = configini.get('list', 'number', data_type=list)
            list_mixed = configini.get('list', 'mixed', data_type=list)
            list_empty = configini.get('list', 'empty', data_type=list)

        cls.config = Config

    def test_list_text(self):
        self.assertEqual(type(self.config.list_text), list)

    def test_list_number(self):
        self.assertEqual(type(self.config.list_number), list)

    def test_list_mixed(self):
        self.assertEqual(type(self.config.list_mixed), list)

    def test_list_empty(self):
        self.assertEqual(type(self.config.list_empty), list)


class TestNone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            none_string = configini.get('none', 'none', data_type=str)
            none_integer = configini.get('none', 'none', data_type=int)
            none_float = configini.get('none', 'none', data_type=float)
            none_list = configini.get('none', 'none', data_type=list)

        cls.config = Config

    def test_none_string(self):
        self.assertIsNone(self.config.none_string)

    def test_none_integer(self):
        self.assertIsNone(self.config.none_integer)

    def test_none_float(self):
        self.assertIsNone(self.config.none_float)

    def test_none_list(self):
        self.assertIsNone(self.config.none_list)


if __name__ == '__main__':
    unittest.main()
