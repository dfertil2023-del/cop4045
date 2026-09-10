import unittest

from p5_Fertil_David import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
	def test_caesar_cipher_normal_message(self):
		self.assertEqual(caesar_cipher("hello", 3), "khoor")

	def test_caesar_cipher_uppercase_spaces_and_punctuation(self):
		self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

	def test_caesar_cipher_wraparound(self):
		self.assertEqual(caesar_cipher("xyz XYZ", 3), "abc ABC")

	def test_caesar_cipher_negative_shift(self):
		self.assertEqual(caesar_cipher("def DEF", -3), "abc ABC")


class TestCaesarDecipher(unittest.TestCase):
	def test_caesar_decipher_normal_message(self):
		self.assertEqual(caesar_decipher("khoor", 3), "hello")

	def test_caesar_decipher_uppercase_spaces_and_punctuation(self):
		self.assertEqual(caesar_decipher("Khoor, Zruog!", 3), "Hello, World!")

	def test_caesar_decipher_wraparound(self):
		self.assertEqual(caesar_decipher("abc ABC", 3), "xyz XYZ")

	def test_caesar_decipher_negative_shift(self):
		self.assertEqual(caesar_decipher("abc ABC", -3), "def DEF")


class TestLetterFrequency(unittest.TestCase):
	def test_letter_frequency_normal_message(self):
		frequency = letter_frequency("hello")
		self.assertEqual(frequency["h"], 1)
		self.assertEqual(frequency["e"], 1)
		self.assertEqual(frequency["l"], 2)
		self.assertEqual(frequency["o"], 1)

	def test_letter_frequency_ignores_case_spaces_and_punctuation(self):
		frequency = letter_frequency("Aa! B-b 123")
		self.assertEqual(frequency["a"], 2)
		self.assertEqual(frequency["b"], 2)
		self.assertEqual(sum(frequency.values()), 4)

	def test_letter_frequency_includes_all_letters(self):
		frequency = letter_frequency("")
		self.assertEqual(len(frequency), 26)
		self.assertTrue(all(count == 0 for count in frequency.values()))


if __name__ == "__main__":
	unittest.main()
