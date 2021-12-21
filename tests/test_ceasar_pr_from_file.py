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
