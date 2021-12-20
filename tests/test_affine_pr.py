import unittest
from parameterized import *
from src.sample.Affine import *
class Affine_test_parameterized(unittest.TestCase):
    def setUp(self):
        self.temp = Affine()

    @parameterized.expand([
        ('veni', 3, 12, 'xyzk'),
        ('VINI', 3, 32, 'RETE'),
        ('dici', 2, 16, 'wgug'),
        ('IL', 5, 15, 'DS'),
        ('DUCE',25 ,25, 'WFXV' )
    ])

    def test_affine_words(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

