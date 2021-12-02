import unittest
import irreversible_tokenization as it

class TestIrreversibleTokenization(unittest.TestCase):
    def test_hash_token(self):
        next_token = it.hash_token("79927398713")
        self.assertEqual(next_token, "15670504099")

        for i in range(10):
            next_token = it.hash_token(next_token)
            self.assertTrue(it.luhn(str(next_token)))

    def test_hash_token_raises_on_invalid_input(self):
        s = "79927398712"
        with self.assertRaises(ValueError):
            it.hash_token(s)

    def test_mac_token(self):
        key = "secret"
        next_token = it.mac_token(key, "79927398713")
        self.assertEqual(next_token, "65140041396")

        for i in range(10):
            next_token = it.mac_token(key, next_token)
            self.assertTrue(it.luhn(str(next_token)))

    def test_mac_token_raises_on_invalid_input(self):
        s = "79927398712"
        with self.assertRaises(ValueError):
            it.mac_token("secret", s)


class TestLuhnChecksum(unittest.TestCase):
    def test_calculation(self):
        s = "7992739871"
        checksum = it.calculate_luhn_checksum(s)
        self.assertEqual(checksum, 3)

        s = "13482517501235"
        checksum = it.calculate_luhn_checksum(s)
        self.assertEqual(checksum, 9)

    def test_calculation_raises_on_invalid_number(self):
        s = "79helloworld"
        with self.assertRaises(ValueError):
            it.calculate_luhn_checksum(s)

    def test_verification(self):
        s = "79927398713"
        self.assertTrue(it.luhn(s))

        s = "79927398714"
        self.assertFalse(it.luhn(s))

    def test_verification_raises_on_invalid_number(self):
        s = "7992739871x"
        with self.assertRaises(ValueError):
            it.luhn(s)

    def test_validation_raises_on_too_short_number(self):
        s = "3"
        with self.assertRaises(ValueError):
            it.luhn(s)

if __name__ == '__main__':
    unittest.main()
