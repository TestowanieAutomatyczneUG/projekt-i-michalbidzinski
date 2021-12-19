import unittest
from hamcrest import *
from src.sample.Ceasar import Ceasar
class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Ceasar()
    def test_ceasar_letter(self):
        assert_that(self.temp.encrypt('a'), equal_to('d'))
    def test_ceasar_word(self):
        assert_that(self.temp.encrypt('VENI'), equal_to('YHQL'))
    def test_ceasar_word_lowercase(self):
        assert_that(self.temp.encrypt('veni'), equal_to('yhql'))
    def test_ceasar_last_3_letters(self):
        assert_that(self.temp.encrypt('XYZ'), equal_to('UVW'))
    def test_ceasar_last_3_letters_lowercase(self):
        assert_that(self.temp.encrypt('xyz'), equal_to('uvw'))
    def test_ceasar_whole_alphabet(self):
        assert_that(self.temp.encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), equal_to('DEFGHIJKLMNOPQRSTUVWXYZUVW'))
    def test_ceasar_whole_alphabet_lowercase(self):
        assert_that(self.temp.encrypt('abcdefghijklmnopqrstuvxyz'), equal_to('defghijklmnopqrstuvwxyuvw'))
    def test_ceasar_sentence(self):
        assert_that(self.temp.encrypt('hello world'), equal_to('khoor zruog'))
    def test_ceasar_sentence_2(self):
        assert_that(self.temp.encrypt('ala ma kota'), equal_to('dod pd nrwd'))
    def test_ceasar_with_multiple_spaces(self):
        assert_that(self.temp.encrypt('ala     ma   kota'), equal_to('dod     pd   nrwd'))
    def test_ceasar_not_in_alphabet(self):
        assert_that(calling(self.temp.encrypt).with_args('2'), raises(Exception))





