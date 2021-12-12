import unittest
from src.sample.Morse import  Morse
import assertpy
class TestMorse(unittest.TestCase):
    def setUp(self):
        self.temp = Morse()
    def test_morse_single_letter(self):
        morse=".- "
        inputed_data = "A"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_word(self):
        morse=".-- --- -.. .- "
        inputed_data = "woda"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_numbers(self):
        morse=".---- ..--- ...-- "
        inputed_data="123"
        self.assertEqual(morse,self.temp.coding(inputed_data))
    def test_morse_sentence(self):
        morse=".- .-.. .-  -- .-  -.- --- - .- "
        inputed_data = "Ala ma kota"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_empty(self):
        morse = ""
        inputed_data = ""
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_punctuation_marks(self):
        morse = "--..-- "
        inputed_data = ","
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_punctuation_marks_2(self):
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-. "
        inputed_data = "&'@)(:,=!.-+\"?/"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_with_polish_marks(self):
        morse = '.-.- -.-.. ..-.. .-..- --.-- ---. ...-... --..-. --..- ...-...'
        inputed_data = "ąćęłńóśźżś"
        self.assertEqual(morse, self.temp.coding(inputed_data))







    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
