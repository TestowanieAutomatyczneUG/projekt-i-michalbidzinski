import unittest
from src.sample.Ceasar import *
import json
class CeasarTestFromFile(unittest.TestCase):
    def test_Ceasar_encrypt_from_jsonFile(self):
        jsonFile = open("../data/data.json")
        ceasar = Ceasar()
        testData = json.loads(jsonFile.read())
        for [input, expectedOutput] in testData:
            self.assertEqual(ceasar.encrypt(input), expectedOutput)
