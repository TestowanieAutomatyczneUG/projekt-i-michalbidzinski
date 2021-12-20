import unittest
from parameterized import *
from src.sample.Affine import *
class Affine_test_parameterized(unittest.TestCase):
    def setUp(self):
        self.temp = Affine()

    @parameterized.expand([
        ('VENI', 3, 12, 'XYZK')
    ])
    def test_affine_3_12_VENI(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

