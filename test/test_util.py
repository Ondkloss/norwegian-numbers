import unittest
import norwegian_numbers.util as internal
import norwegian_numbers as nn


class TestKid(unittest.TestCase):

    # MOD10CD tests
    def test_mod10_control_digit(self):
        self.assertEqual(6, internal.make_mod10_control_digit('234567', [2, 1]))

    def test_mod10_control_digit_0(self):
        self.assertEqual(0, internal.make_mod10_control_digit('0', [2, 1]))

    def test_mod10_control_digit_error(self):
        with self.assertRaises(ValueError):
            internal.make_mod10_control_digit('abc', [2, 1])

    def test_mod10_control_digit_error_blank(self):
        with self.assertRaises(ValueError):
            internal.make_mod10_control_digit('', [2, 1])

    # MOD11CD tests
    def test_mod11_control_digit(self):
        self.assertEqual(3, internal.make_mod11_control_digit('1234567890', [2, 3, 4, 5, 6, 7]))

    def test_mod11_control_digit_0(self):
        self.assertEqual(0, internal.make_mod11_control_digit('31', [2, 3, 4, 5, 6, 7]))

    def test_mod11_control_digit_dash(self):
        self.assertEqual('-', internal.make_mod11_control_digit('40', [2, 3, 4, 5, 6, 7]))

    def test_mod10_control_digit_error(self):
        with self.assertRaises(ValueError):
            internal.make_mod11_control_digit('abc', [2, 3, 4, 5, 6, 7])

    def test_mod11_control_digit_error_blank(self):
        with self.assertRaises(ValueError):
            internal.make_mod11_control_digit('', [2, 3, 4, 5, 6, 7])

    # KID tests
    def test_kid_mod10(self):
        self.assertEqual('2345676', nn.make_kid_number('234567'))
        self.assertTrue(nn.verify_kid_number('2345676'))

    def test_kid_mod10_0(self):
        self.assertEqual('00', nn.make_kid_number('0'))

    def test_kid_mod10_0(self):
        self.assertEqual('00', nn.make_kid_number('0'))

    def test_kid_mod10_error(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('abc')

    def test_kid_mod10_error_len(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('01234567890123456789012345')

    def test_kid_mod11_error_blank(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('', 'MOD11')

    def test_kid_mod11(self):
        self.assertEqual('12345678903', nn.make_kid_number('1234567890', 'MOD11'))
        self.assertTrue(nn.verify_kid_number('12345678903', 'MOD11'))

    def test_kid_mod11_0(self):
        self.assertEqual('310', nn.make_kid_number('31', 'MOD11'))

    def test_kid_mod11_dash(self):
        self.assertEqual('40-', nn.make_kid_number('40', 'MOD11'))

    def test_kid_mod11_error(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('abc', 'MOD11')

    def test__kid_mod11_error_len(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('01234567890123456789012345', 'MOD11')

    def test_kid_mod11_error_blank(self):
        with self.assertRaises(ValueError):
            nn.make_kid_number('', 'MOD11')

    # Account number tests
    def test_account_number(self):
        self.assertEqual('12345678903', nn.make_account_number('1234567890'))
        self.assertTrue(nn.verify_account_number('12345678903'))

    def test_account_number_error(self):
        with self.assertRaises(ValueError):
            nn.make_account_number('0000002001')
        self.assertFalse(nn.verify_account_number('0000002001-'))

    # Organisation number tests
    def test_organisation_number(self):
        self.assertEqual('123456785', nn.make_organisation_number('12345678'))
        self.assertTrue(nn.verify_organisation_number('123456785'))

    def test_organisation_number_error(self):
        with self.assertRaises(ValueError):
            nn.make_organisation_number('00002001')
        self.assertFalse(nn.verify_organisation_number('00002001-'))

    # Birth number tests
    def test_birth_number(self):
        self.assertEqual('31129956715', nn.make_birth_number('311299567'))
        self.assertTrue(nn.verify_birth_number('31129956715'))

    def test_birth_number_error_1(self):
        with self.assertRaises(ValueError):
            nn.make_birth_number('000000021')
        self.assertFalse(nn.verify_birth_number('000000021-2'))

    def test_birth_number_error_2(self):
        with self.assertRaises(ValueError):
            nn.make_birth_number('101000000')
        self.assertFalse(nn.verify_birth_number('1010000002-'))


if __name__ == '__main__':
    unittest.main()
