import unittest
from src.sample.Morse import  Morse
import assertpy
class TestMorse(unittest.TestCase):
    def setUp(self):
        self.temp = Morse()
    def test_morse_single_letter(self):
        morse=".- "
        expected_output = "A"
        self.assertEqual(morse, self.temp.coding(expected_output))
    def test_morse_word(self):
        morse=".-- --- -.. .- "
        expected_output = "woda"
        self.assertEqual(morse, self.temp.coding(expected_output))
    def test_morse_numbers(self):
        morse=".---- ..--- ...-- "
        expected_output="123"
        self.assertEqual(morse,self.temp.coding(expected_output))
    def test_morse_sentence(self):
        morse=".- .-.. .-  -- .-  -.- --- - .- "
        expected_output = "Ala ma kota"
        self.assertEqual(morse, self.temp.coding(expected_output))

    def test_morse_empty(self):
        morse = ""
        self.assertRaises(Exception, self.temp.coding, morse)




    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
