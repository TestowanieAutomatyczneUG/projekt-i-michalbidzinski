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
    @parameterized.expand([
        ('hello world', 3, 12, 'hyttc acltv'),
        ('witaj swiecie', 3, 12, 'akrmn oakysky'),
        ('WESOLYCH SWIAT', 3, 12, 'AYOCTGSH OAKMR'),
        ('ala ma kota kot ma ALE', 3, 12, 'mtm wm qcrm qcr wm MTY'),
    ])
    def test_affine_sentences(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('123', 3, 12, Exception),
        (',&!2@;.xxxz', 3, 12, 'akrmn oakysky'),
        (1, 3, 12, 'AYOCTGSH OAKMR'),
        (str, 3, 12, 'mtm wm qcrm qcr wm MTY'),
        ([], 3, 12, 'mtm wm qcrm qcr wm MTY'),
        ({}, 3, 12, 'mtm wm qcrm qcr wm MTY'),
        (None, 3, 12, 'mtm wm qcrm qcr wm MTY'),
        (True, 3, 12, 'mtm wm qcrm qcr wm MTY'),
    ])
    def test_affine_wrong_text_provided(self, text, a, b, cipher):
        self.assertRaises(Exception, self.temp.affine_encrpyt, text, a,b,cipher)


