import unittest
from src.sample.Morse import  Morse
class TestMorse(unittest.TestCase):
    def setUp(self):
        self.temp = Morse()
    def test_morse_to_text(self):
        morse=".-"
        expected_output = "A"
        self.assertEqual(morse, self.temp.coding(expected_output))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
