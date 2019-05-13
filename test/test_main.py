import unittest
import norwegian_numbers.__main__ as internal


class TestMain(unittest.TestCase):
    def test_argparser(self):
        args = internal.argparser(['-m', 'kid10', '1234'])
        self.assertEqual('kid10', args.make)
        self.assertEqual(None, args.verify)
        self.assertEqual('1234', args.value)

    def test_main_make_kid10(self):
        result = internal.main(['-m', 'kid10', '1234'])
        self.assertEqual('12344', result)

    def test_main_make_kid11(self):
        result = internal.main(['-m', 'kid11', '1234'])
        self.assertEqual('12343', result)

    def test_main_make_organisation(self):
        result = internal.main(['-m', 'organisation', '12345678'])
        self.assertEqual('123456785', result)

    def test_main_make_birth(self):
        result = internal.main(['-m', 'birth', '311299567'])
        self.assertEqual('31129956715', result)

    def test_main_make_account(self):
        result = internal.main(['-m', 'account', '1234567890'])
        self.assertEqual('12345678903', result)

    def test_main_verify_kid10(self):
        result = internal.main(['-v', 'kid10', '12344'])
        self.assertEqual(True, result)

    def test_main_verify_kid11(self):
        result = internal.main(['-v', 'kid11', '12343'])
        self.assertEqual(True, result)

    def test_main_verify_organisation(self):
        result = internal.main(['-v', 'organisation', '123456785'])
        self.assertEqual(True, result)

    def test_main_verify_birth(self):
        result = internal.main(['-v', 'birth', '31129956715'])
        self.assertEqual(True, result)

    def test_main_verify_account(self):
        result = internal.main(['-v', 'account', '12345678903'])
        self.assertEqual(True, result)
