import decimal
import unittest
import configini


class TestString(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            string_text = configini.String('string', 'text')
            string_integer = configini.String('string', 'integer')
            string_double_quotes = configini.String('string', 'double_quotes')
            string_single_quotes = configini.String('string', 'single_quotes')

        cls.config = Config

    def test_str_text(self):
        self.assertEqual(self.config.string_text, '23')

    def test_str_integer(self):
        self.assertEqual(self.config.string_integer, '1')

    def test_str_double_quotes(self):
        self.assertEqual(self.config.string_double_quotes, '"A"')

    def test_str_single_quotes(self):
        self.assertEqual(self.config.string_single_quotes, '\'A\'')


class TestInteger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            zero = configini.Integer('number', 'zero')
            one = configini.Integer('number', 'one')
            negative_one = configini.Integer('number', 'negative_one')

        cls.config = Config

    def test_integer_zero(self):
        self.assertEqual(self.config.zero, 0)

    def test_integer_one(self):
        self.assertEqual(self.config.one, 1)

    def test_integer_negative_one(self):
        self.assertEqual(self.config.negative_one, -1)


class TestFloat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            zero = configini.Float('number', 'zero')
            one = configini.Float('number', 'one')
            negative_one = configini.Float('number', 'negative_one')
            zero_with_dot = configini.Float('number', 'zero_with_dot')
            one_with_dot = configini.Float('number', 'one_with_dot')
            negative_one_with_dot = configini.Float('number', 'negative_one_with_dot')
            one_dot_five = configini.Float('number', 'one_dot_five')

        cls.config = Config

    def test_float_zero(self):
        self.assertEqual(self.config.zero, 0)

    def test_float_one(self):
        self.assertEqual(self.config.one, 1)

    def test_float_negative_one(self):
        self.assertEqual(self.config.negative_one, -1)

    def test_float_zero_with_dot(self):
        self.assertEqual(self.config.zero_with_dot, 0.0)

    def test_float_one_with_dot(self):
        self.assertEqual(self.config.one_with_dot, 1.0)

    def test_float_negative_one_with_dot(self):
        self.assertEqual(self.config.negative_one_with_dot, -1.0)

    def test_float_one_dot_five(self):
        self.assertEqual(self.config.one_dot_five, 1.5)


class TestDecimal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            zero = configini.Decimal('number', 'zero')
            one = configini.Decimal('number', 'one')
            negative_one = configini.Decimal('number', 'negative_one')
            zero_with_dot = configini.Decimal('number', 'zero_with_dot')
            one_with_dot = configini.Decimal('number', 'one_with_dot')
            negative_one_with_dot = configini.Decimal('number', 'negative_one_with_dot')
            one_dot_five = configini.Decimal('number', 'one_dot_five')

        cls.config = Config

    def test_decimal_zero(self):
        self.assertEqual(self.config.zero, 0)

    def test_decimal_one(self):
        self.assertEqual(self.config.one, 1)

    def test_decimal_negative_one(self):
        self.assertEqual(self.config.negative_one, -1)

    def test_decimal_zero_with_dot(self):
        self.assertEqual(self.config.zero_with_dot, 0.0)

    def test_decimal_one_with_dot(self):
        self.assertEqual(self.config.one_with_dot, 1.0)

    def test_decimal_negative_one_with_dot(self):
        self.assertEqual(self.config.negative_one_with_dot, -1.0)

    def test_decimal_one_dot_five(self):
        self.assertEqual(self.config.one_dot_five, 1.5)


class TestBool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            bool_1 = configini.Boolean('bool', '1')
            bool_true = configini.Boolean('bool', 'true')
            bool_yes = configini.Boolean('bool', 'yes')
            bool_0 = configini.Boolean('bool', '0')
            bool_false = configini.Boolean('bool', 'false')
            bool_no = configini.Boolean('bool', 'no')

        cls.config = Config

    def test_bool_1(self):
        self.assertTrue(self.config.bool_1)

    def test_bool_true(self):
        self.assertTrue(self.config.bool_true)

    def test_bool_yes(self):
        self.assertTrue(self.config.bool_yes)

    def test_bool_0(self):
        self.assertFalse(self.config.bool_0)

    def test_bool_false(self):
        self.assertFalse(self.config.bool_false)

    def test_bool_no(self):
        self.assertFalse(self.config.bool_no)


class TestList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            list_text = configini.List('list', 'text')
            list_number = configini.List('list', 'number')
            list_mixed = configini.List('list', 'mixed')
            list_empty = configini.List('list', 'empty')

        cls.config = Config

    def test_list_text(self):
        self.assertEqual(self.config.list_text, ["A", "B", "C"])

    def test_list_number(self):
        self.assertEqual(self.config.list_number, [1, 2, 3])

    def test_list_mixed(self):
        self.assertEqual(self.config.list_mixed, ["A", 1, False])

    def test_list_empty(self):
        self.assertEqual(self.config.list_empty, [])


class TestDict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            dict_text = configini.Dict('dict', 'text')
            dict_list = configini.Dict('dict', 'list')
            dict_empty = configini.Dict('dict', 'empty')

        cls.config = Config

    def test_dict_text(self):
        self.assertEqual(self.config.dict_text, {"A": 1})

    def test_dict_number(self):
        self.assertEqual(self.config.dict_list, {"list": [1, 2, 3]})

    def test_dict_empty(self):
        self.assertEqual(self.config.dict_empty, {})


class TestNone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configini.read('config_data_types.ini')

        class Config:
            none_string = configini.String('none', 'none')
            none_integer = configini.Integer('none', 'none')
            none_float = configini.Float('none', 'none')
            none_decimal = configini.Decimal('none', 'none')
            none_boolean = configini.Boolean('none', 'none')
            none_list = configini.List('none', 'none')
            none_dict = configini.Dict('none', 'none')

        cls.config = Config

    def test_none_string(self):
        self.assertIsNone(self.config.none_string)

    def test_none_integer(self):
        self.assertIsNone(self.config.none_integer)

    def test_none_float(self):
        self.assertIsNone(self.config.none_float)

    def test_none_decimal(self):
        self.assertIsNone(self.config.none_decimal)

    def test_none_boolean(self):
        self.assertIsNone(self.config.none_boolean)

    def test_none_list(self):
        self.assertEqual(self.config.none_list, [])

    def test_none_dict(self):
        self.assertEqual(self.config.none_dict, {})


if __name__ == '__main__':
    unittest.main()
