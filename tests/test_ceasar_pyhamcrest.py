import unittest
from hamcrest import *

from src.sample.Ceasar import Ceasar



class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Ceasar()


    # ENCRPYT
    def test_ceasar_letter(self):
        assert_that(self.temp.encrypt('a'), equal_to('d'))

    def test_ceasar_word(self):
        assert_that(self.temp.encrypt('VENI'), equal_to('YHQL'))

    def test_ceasar_word_lowercase(self):
        assert_that(self.temp.encrypt('veni'), equal_to('yhql'))

    def test_ceasar_last_3_letters(self):
        assert_that(self.temp.encrypt('XYZ'), equal_to('ABC'))

    def test_ceasar_last_3_letters_lowercase(self):
        assert_that(self.temp.encrypt('xYz'), equal_to('aBc'))

    def test_ceasar_whole_alphabet(self):
        assert_that(self.temp.encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), equal_to('DEFGHIJKLMNOPQRSTUVWXYZABC'))

    def test_ceasar_whole_alphabet_lowercase(self):
        assert_that(self.temp.encrypt('abcdefghijklmnopqrstuvxyz'), equal_to('defghijklmnopqrstuvwxyabc'))

    def test_ceasar_sentence(self):
        assert_that(self.temp.encrypt('hellO woRld'), equal_to('khooR zrUog'))

    def test_ceasar_sentence_2(self):
        assert_that(self.temp.encrypt('ala ma kota'), equal_to('dod pd nrwd'))

    def test_ceasar_with_multiple_spaces(self):
        assert_that(self.temp.encrypt('ala     ma   kota'), equal_to('dod     pd   nrwd'))

    # ENCRPYT exceptions
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

    # DECRYPT
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

    def test_ceasar_decrypt_whole_alphabet(self):
        assert_that(self.temp.decrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), equal_to('XYZABCDEFGHIJKLMNOPQRSTUVW'))

    def test_ceasar_decrypt_whole_alphabet_lowercase(self):
        assert_that(self.temp.decrypt('abcdefghijklmnopqrstuvxyz'), equal_to('xyzabcdefghijklmnopqrsuvw'))

    def test_ceasar_decrypt_sentence(self):
        assert_that(self.temp.decrypt('hello world'), equal_to('ebiil tloia'))

    def test_ceasar_decrypt_sentence_2(self):
        assert_that(self.temp.decrypt('ala ma kota'), equal_to('xix jx hlqx'))

    def test_ceasar_decrypt_with_multiple_spaces(self):
        assert_that(self.temp.decrypt('ala     ma   kota'), equal_to('xix     jx   hlqx'))

    def test_ceasar_decypt_empty(self):
        assert_that(self.temp.decrypt(''), equal_to(''))

    # DECRYPT exceptions
    def test_ceasar_decrypt_not_in_alphabet(self):
        assert_that(calling(self.temp.decrypt).with_args('2'), raises(Exception))

    def test_ceasar_decrypt_None(self):
        assert_that(calling(self.temp.decrypt).with_args(None), raises(Exception))

    def test_ceasar_decrypt_True(self):
        assert_that(calling(self.temp.decrypt).with_args(True), raises(Exception))

    def test_ceasar_decrypt_False(self):
        assert_that(calling(self.temp.decrypt).with_args(False), raises(Exception))

    def test_ceasar_decrypt_arr(self):
        assert_that(calling(self.temp.decrypt).with_args([]), raises(Exception))

    def test_ceasar_decrypt_obj(self):
        assert_that(calling(self.temp.decrypt).with_args({}), raises(Exception))

    def test_ceasar_decrypt_int(self):
        assert_that(calling(self.temp.decrypt).with_args(3), raises(Exception))

    def test_ceasar_decrypt_float(self):
        assert_that(calling(self.temp.decrypt).with_args(3.14), raises(Exception))

    # użycie róznych matcherów z pyhamcresta
    def test_ceasar_has_length(self):
        assert_that(self.temp.decrypt('abc'), has_length(3))

    def test_ceasar_has_string(self):
        assert_that(self.temp.decrypt('abc'), has_string('xyz'))

    def test_ceasar_constains_string(self):
        assert_that(self.temp.decrypt('abc'), contains_string('x'))

    def test_ceasar_ends_with(self):
        assert_that(self.temp.decrypt('abc'), ends_with('z'))

    def test_ceasar_starts_with(self):
        assert_that(self.temp.decrypt('abc'), starts_with('x'))

    def test_ceasar_string_contains_in_order(self):
        assert_that(self.temp.decrypt('abcdefgh'), string_contains_in_order('xyz'))

    def test_ceasar_equal_to_ignoring_case(self):
        assert_that(self.temp.decrypt('abc'), equal_to_ignoring_case('XYZ'))

    def test_ceasar_instance_of(self):
        assert_that(self.temp.decrypt('abc'), instance_of(str))
