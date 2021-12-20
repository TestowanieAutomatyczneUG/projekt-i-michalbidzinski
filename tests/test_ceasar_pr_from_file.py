import unittest
from src.sample.Ceasar import Ceasar
import json

class CeasarTestFromFile(unittest.TestCase):
    def test_Ceasar_encrypt_from_jsonFile(self):
        # data = open("../data/data.json")
        jsonFile = open("C:/Users/mbidz/PycharmProjects/projekt-i-michalbidzinski/data/data.json")
        ceasar = Ceasar()
        testData = json.loads(jsonFile.read())
        for [input, expectedOutput] in testData:
            self.assertEqual(ceasar.encrypt(input), expectedOutput)

    def test_Ceasar_encrypt_exceptions_from_jsonFile(self):
        # data = open("../data/dataExceptions.json")
        jsonFile = open("C:/Users/mbidz/PycharmProjects/projekt-i-michalbidzinski/data/dataExceptions.json")
        ceasar = Ceasar()
        testData = json.loads(jsonFile.read())
        for input in testData:
            self.assertRaises(Exception, ceasar.encrypt, input)
    def test_Ceasar_encrypt_from_file_word(self):
        # data = open("../data/data")
        data = open("C:/Users/mbidz/PycharmProjects/projekt-i-michalbidzinski/data/data")
        ceasar = Ceasar()
        for lines in data:
            line = lines.split(" ")
            input, output = line[0], line[1].strip("\n")
            self.assertEqual(ceasar.encrypt(input), output)
    def test_Ceasar_encrypt_from_file_sentence_with_spaces(self):
        # data = open("../data/dataWithSpaces")
        data = open("C:/Users/mbidz/PycharmProjects/projekt-i-michalbidzinski/data/dataWithSpaces")
        ceasar = Ceasar()
        for lines in data:
            line = lines.split(" ")
            input, output = line[0] + " " +  line[1], line[2].strip("\n") + " " +  line[3].strip("\n")
            self.assertEqual(ceasar.encrypt(input), output)
    def test_Ceasar_encrypt_from_file_word_exceptions(self):
        # data = open("../data/dataExceptions")
        data = open("C:/Users/mbidz/PycharmProjects/projekt-i-michalbidzinski/data/dataExceptions")
        ceasar = Ceasar()
        for lines in data:
            line = lines.split(" ")
            input = line[0]
            self.assertRaises(Exception, ceasar.encrypt, input)
