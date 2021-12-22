import unittest
import pytest
from src.sample.Ceasar import Ceasar


class TestCeasarPytest(unittest.TestCase):
    def setUp(self):
        self.temp = Ceasar()

    def test_a_should_be_encrypted_to_d(self):
        assert self.temp.encrypt('a') == 'd'

    def test_ab_should_be_encrypted_to_de(self):
        assert self.temp.encrypt('ab') == 'de'

    def test_z_should_be_encrypted_to_c(self):
        assert self.temp.encrypt('z') == 'c'

    def test_A_should_be_encrypted_to_D(self):
        assert self.temp.encrypt('A') == 'D'

    def test_Z_should_be_encrypted_to_C(self):
        assert self.temp.encrypt('Z') == 'C'

    def test_encrypt_whole_alphabet(self):
        assert self.temp.encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    def test_encrypt_sentence(self):
        assert self.temp.encrypt('hellO woRld') == 'khooR zrUog'

    def test_encrypt_sentence_2(self):
        assert self.temp.encrypt('ala ma kota') == 'dod pd nrwd'

    def test_encrypt_raise_exception_when_str_not_in_alphabet(self):
        with pytest.raises(Exception):
            self.temp.encrypt('2')

    def test_encrypt_raise_exception_when_None(self):
        with pytest.raises(Exception):
            self.temp.encrypt(None)

    def test_encrypt_raise_exception_when_True(self):
        with pytest.raises(Exception):
            self.temp.encrypt(True)

    def test_encrypt_raise_exception_when_False(self):
        with pytest.raises(Exception):
            self.temp.encrypt(False)

    def test_encrypt_raise_exception_when_array(self):
        with pytest.raises(Exception):
            self.temp.encrypt([])

    def test_encrypt_raise_exception_when_obj(self):
        with pytest.raises(Exception):
            self.temp.encrypt({})

    def test_encrypt_raise_exception_when_int(self):
        with pytest.raises(Exception):
            self.temp.encrypt(3)

    def test_encrypt_raise_exception_when_float(self):
        with pytest.raises(Exception):
            self.temp.encrypt(3.14)

    def test_a_should_be_decrypted_to_x(self):
        assert self.temp.decrypt('a') == 'x'

    def test_alphabet_should_be_decrypted_to_XYZABCDEFGHIJKLMNOPQRSTUVW(self):
        assert self.temp.decrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'XYZABCDEFGHIJKLMNOPQRSTUVW'

    def test_sentence_should_be_decrypted(self):
        assert self.temp.decrypt('hello world') == 'ebiil tloia'

    def test_decrypt_raise_exception_when_str_not_in_alphabet(self):
        with pytest.raises(Exception):
            self.temp.decrypt('2')

