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
        ('DUCE',25 ,25, 'WFXV' ),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3, 12, 'MPSVYBEHKNQTWZCFILORUXADGJ'),
    ])

    def test_affine_words(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('a', 3, 12, 'm'),
        ('B', 3, 12, 'P'),
        ('c', 3, 12, 's'),
        ('X', 3, 12, 'D'),
        ('y', 3, 12, 'g'),
        ('Z', 3, 12, 'J')
    ])
    def test_affine_single_letters(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

