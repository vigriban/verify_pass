import unittest
import verify_pass

MAX_STRENGTH_PASS = '!1Aa' + 9 * '!'
MAX_SCORE = 14


class PasswordTest(unittest.TestCase):

    def test_empty_password_has_zero_score(self):
        self.assertEqual(verify_pass.verify_password(''), 0)

    def test_max_strength_pass(self):
        self.assertEqual(
            verify_pass.verify_password(MAX_STRENGTH_PASS),
            MAX_SCORE
        )

    def test_max_strength_pass_without_special(self):
        password = MAX_STRENGTH_PASS.replace('!', '1')
        self.assertEqual(
            verify_pass.verify_password(password),
            MAX_SCORE - verify_pass.STRENGTH_POINTS
        )

    def test_short_max_strength_pass(self):
        password = MAX_STRENGTH_PASS[:-1]
        self.assertEqual(
            verify_pass.verify_password(password),
            MAX_SCORE - verify_pass.STRENGTH_POINTS
        )

    def test_max_strength_pass_without_upper(self):
        password = MAX_STRENGTH_PASS.replace('A', 'a')
        self.assertEqual(
            verify_pass.verify_password(password),
            MAX_SCORE - verify_pass.STRENGTH_POINTS
        )

    def test_max_strength_pass_without_lower(self):
        password = MAX_STRENGTH_PASS.replace('a', 'A')
        self.assertEqual(
            verify_pass.verify_password(password),
            MAX_SCORE - verify_pass.STRENGTH_POINTS
        )

    def test_max_strength_pass_without_lower(self):
        password = MAX_STRENGTH_PASS.replace('a', 'A')
        self.assertEqual(
            verify_pass.verify_password(password),
            MAX_SCORE - verify_pass.STRENGTH_POINTS
        )


if __name__ == '__main__':
    unittest.main()
