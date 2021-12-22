import unittest
from src.sample.Morse import *
from assertpy import *
# własny matcher
import re


def check_if_morse_has_more_dots_than_dashes(self, text):
    if self.val.count(".") > self.val.count("-"):
        return self
    return self.error("Jest więcej lub porówno kropek co kresek w kodzie morsa")


def check_if_decrypted_morse_is_uppercase_and_has_nums_and_special_makrs(self, str):
    regex = ("(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@$%^&*., ?]).+$")
    p = re.compile(regex)

    if re.search(p, self.val):
        return self
    else:
        return self.error("Rozszyfrowana wiadomosc nie ma albo liczb albo znakow interpunkcyjnych")


add_extension(check_if_decrypted_morse_is_uppercase_and_has_nums_and_special_makrs)
add_extension(check_if_morse_has_more_dots_than_dashes)


# użycie unittesta i assertpy wymiennie
class TestMorse(unittest.TestCase):
    def setUp(self):
        self.temp = Morse()

    # własny matcher
    def test_morse_check_if_morse_has_more_dots_than_dashes(self):
        #     morse = ".... . .--- "
        inputed_data = 'hej'
        assert_that(self.temp.coding(inputed_data)).check_if_morse_has_more_dots_than_dashes(inputed_data)

    def test_morse_check_if_morse_has_more_dots_than_dashes_2(self):
        # morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-. "
        inputed_data = "&'@)(:,=!.-+\"?/"
        assert_that(self.temp.coding(inputed_data)).check_if_morse_has_more_dots_than_dashes(inputed_data)

    def test_morse_check_if_morse_has_more_dots_than_dashes_3_sentence(self):
        inputed_data = 'hej hej hej '
        assert_that(self.temp.coding(inputed_data)).check_if_morse_has_more_dots_than_dashes(inputed_data)

    def test_morse_check_if_morse_has_more_dots_than_dashes_number(self):
        inputed_data = '4'
        assert_that(self.temp.coding(inputed_data)).check_if_morse_has_more_dots_than_dashes(inputed_data)

    def test_morse_check_if_morse_has_more_dots_than_dashes_number_lk(self):
        inputed_data = 'lk'
        assert_that(self.temp.coding(inputed_data)).check_if_morse_has_more_dots_than_dashes(inputed_data)

    def test_morse_check_if_morse_has_upper_case_nums_and_special_marks_word(self):
        morse = ".... . .-.. .-.. --- .-- --- .-. .-.. -.. .---- ..--- ...-- .--.-."
        assert_that(self.temp.decoding(morse)).check_if_decrypted_morse_is_uppercase_and_has_nums_and_special_makrs(
            morse)

    def test_morse_check_if_morse_has_upper_case_nums_and_special_marks_sentence(self):
        morse = ".... .. .--.-.     .-- .---- - ....- --"
        assert_that(self.temp.decoding(morse)).check_if_decrypted_morse_is_uppercase_and_has_nums_and_special_makrs(
            morse)

    # main program
    def test_morse_single_letter(self):
        morse = ".- "
        inputed_data = "A"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_word(self):
        morse = ".-- --- -.. .- "
        inputed_data = "woda"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_word_new_line(self):
        morse = ".-- ---" \
                " -.. .- "
        inputed_data = "wo" \
                       "da"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_word_2(self):
        morse = ".... --- .--. "
        inputed_data = "hop"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_numbers(self):
        inputed_data = "1234567890"
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- "
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_sentence(self):
        morse = ".- .-.. .-     -- .-     -.- --- - .- "
        inputed_data = "ala ma kota"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_sentence_2(self):
        morse = "-- .- -- .-     -- -. .. .     -... .- .-. -.. --.. ---     .-.. ..- -... .. "
        inputed_data = "mama mnie bardzo lubi"
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
        morse = '.-.- -.-.. ..-.. .-..- --.-- ---. ...-... '
        inputed_data = "ĄĆĘŁŃÓŚ"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    # Exceptions  coding
    def test_morse_coding_float(self):
        inputed_data = 3.14
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)

    def test_morse_coding_False(self):
        inputed_data = False
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)

    def test_morse_coding_True(self):
        inputed_data = True
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)

    def test_morse_coding_None(self):
        inputed_data = None
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)

    def test_morse_coding_invalid_mark_1(self):
        assert_that(self.temp.coding).raises(Exception).when_called_with('¿')

    def test_morse_coding_invalid_mark_2(self):
        assert_that(self.temp.coding).raises(Exception).when_called_with('❤')

    # -------
    # DECODING
    # ----

    def test_morse_decoding_single_letter(self):
        expected_output = "A"
        morse = ".-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_single_word(self):
        expected_output = "ALIBABA"
        morse = ".- .-.. .. -... .- -... .-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_sentence(self):
        expected_output = "ALA MA"
        morse = ".- .-.. .-     -- .-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_sentence_2(self):
        expected_output = "MAMA MNIE BARDZO LUBI"
        morse = "-- .- -- .-     -- -. .. .     -... .- .-. -.. --.. ---     .-.. ..- -... .."
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_punctuation(self):
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:, ,=!.-+\"?/"
        self.assertEqual(self.temp.decoding(morse), expected_output)

    def test_morse_decoding_numbers(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    # Exceptions decoding
    def test_morse_decoding_arr(self):
        self.assertRaises(Exception, self.temp.decoding, [])

    def test_morse_decoding_obj(self):
        self.assertRaises(Exception, self.temp.decoding, {})

    def test_morse_decoding_True(self):
        self.assertRaises(Exception, self.temp.decoding, True)

    def test_morse_decoding_False(self):
        self.assertRaises(Exception, self.temp.decoding, False)

    def test_morse_decoding_float(self):
        self.assertRaises(Exception, self.temp.decoding, 3.14)

    def test_morse_decoding_int(self):
        self.assertRaises(Exception, self.temp.decoding, 3)

    def test_morse_decoding_empty_string(self):
        self.assertRaises(Exception, self.temp.decoding, "")

    def test_morse_decoding_empty_normal_alpahbet(self):
        self.assertRaises(Exception, self.temp.decoding, "hello world")

    def test_morse_decoding_empty_normal_alpahbet_2(self):
        self.assertRaises(Exception, self.temp.decoding, "abcd?")

    def test_morse_decoding_no_such_letter_in_morse_alphabet(self):
        assert_that(self.temp.decoding).raises(Exception).when_called_with('-.-.-.-.--.-')

    def test_morse_decoding_no_such_letter_in_morse_alphabet_2(self):
        assert_that(self.temp.decoding).raises(Exception).when_called_with('-------')

    def test_morse_decoding_no_such_letter_in_morse_alphabet_3(self):
        assert_that(self.temp.decoding).raises(Exception).when_called_with('........')

    def test_morse_decoding_found_4_spaces_in_morse(self):
        assert_that(self.temp.decoding).raises(Exception).when_called_with(
            ".- .-.. .-    -- .-")

    def test_morse_decoding_found_4_spaces_in_morse_2(self):
        assert_that(self.temp.decoding).raises(Exception).when_called_with(
            "-- .- -- .-    -- -. .. .    -... .- .-. -.. --.. ---    .-.. ..- -... ..")

    # rózne asercje w assertpy
    def test_morse_decoding_is_insance_of(self):
        morse = ".-"
        assert_that(self.temp.decoding(morse)).is_instance_of(str)

    def test_morse_is_lenght(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        assert_that(self.temp.decoding(morse)).is_length(len(expected_output))

    def test_morse_is_not_equal_to(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        # expected_output = "1234567890"
        assert_that(self.temp.decoding(morse)).is_not_equal_to("123")

    def test_morse_is_not_none(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        assert_that(self.temp.decoding(morse)).is_not_none()

    def test_morse_contains(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        # expected_output = "1234567890"
        assert_that(self.temp.decoding(morse)).contains("123")

    def test_morse_is_empty(self):
        morse = ""
        assert_that(self.temp.coding(morse)).is_empty()

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
