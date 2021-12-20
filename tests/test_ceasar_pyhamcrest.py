import unittest
from hamcrest import *
from src.sample.Ceasar import Ceasar
class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Ceasar()
    # ecnrypt
    def test_ceasar_letter(self):
        assert_that(self.temp.encrypt('a'), equal_to('d'))
    def test_ceasar_word(self):
        assert_that(self.temp.encrypt('VENI'), equal_to('YHQL'))
    def test_ceasar_word_lowercase(self):
        assert_that(self.temp.encrypt('veni'), equal_to('yhql'))
    def test_ceasar_last_3_letters(self):
        assert_that(self.temp.encrypt('XYZ'), equal_to('ABC'))
    def test_ceasar_last_3_letters_lowercase(self):
        assert_that(self.temp.encrypt('xyz'), equal_to('abc'))
    def test_ceasar_whole_alphabet(self):
        assert_that(self.temp.encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), equal_to('DEFGHIJKLMNOPQRSTUVWXYZABC'))
    def test_ceasar_whole_alphabet_lowercase(self):
        assert_that(self.temp.encrypt('abcdefghijklmnopqrstuvxyz'), equal_to('defghijklmnopqrstuvwxyabc'))
    def test_ceasar_sentence(self):
        assert_that(self.temp.encrypt('hello world'), equal_to('khoor zruog'))
    def test_ceasar_sentence_2(self):
        assert_that(self.temp.encrypt('ala ma kota'), equal_to('dod pd nrwd'))
    def test_ceasar_with_multiple_spaces(self):
        assert_that(self.temp.encrypt('ala     ma   kota'), equal_to('dod     pd   nrwd'))
    # exceptions
    def test_ceasar_not_in_alphabet(self):
        assert_that(calling(self.temp.encrypt).with_args('2'), raises(Exception))
    def test_ceasar_None(self):
        assert_that(calling(self.temp.encrypt).with_args(None), raises(Exception))
    def test_ceasar_True(self):
        assert_that(calling(self.temp.encrypt).with_args(True), raises(Exception))
    def test_ceasar_False(self):
        assert_that(calling(self.temp.encrypt).with_args(False), raises(Exception))
    def test_ceasar_arr(self):
        assert_that(calling(self.temp.encrypt).with_args([]), raises(Exception))

    def test_ceasar_obj(self):
        assert_that(calling(self.temp.encrypt).with_args({}), raises(Exception))

    def test_ceasar_int(self):
        assert_that(calling(self.temp.encrypt).with_args(3), raises(Exception))

    def test_ceasar_float(self):
        assert_that(calling(self.temp.encrypt).with_args(3.14), raises(Exception))
    # decrypt
    def test_ceasar_decrypt_letter(self):
        assert_that(self.temp.decrypt('a'), equal_to('x'))

    def test_ceasar_decryp_decryp_word(self):
        assert_that(self.temp.decrypt('VENI'), equal_to('SBKF'))

    def test_ceasar_decryp_word_lowercase(self):
        assert_that(self.temp.decrypt('veni'), equal_to('sbkf'))

    def test_ceasar_decryp_last_3_letters(self):
        assert_that(self.temp.decrypt('XYZ'), equal_to('UVW'))

    def test_ceasar_decryp_last_3_letters_lowercase(self):
        assert_that(self.temp.decrypt('xyz'), equal_to('uvw'))

 



