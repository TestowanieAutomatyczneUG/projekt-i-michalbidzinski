# class Ceasar:
#     def __init__(self):
#         self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#                          't', 'u', 'v', 'w', 'x', 'y', 'z', ]
#     def encrypt(self, text):
#
#         """
#         >>> g = Ceasar()
#         >>> g.encrypt('a')
#         'd'
#         >>> g.encrypt('VENI')
#         'YHQL'
#         >>> g.encrypt('XYZ')
#         'ABC'
#         >>> g.encrypt('xyz')
#         'abc'
#         >>> g.encrypt('abcdefghijklmnopqrstuvxyz')
#         'defghijklmnopqrstuvwxyabc'
#
#         >>> g.encrypt('hello world')
#         'khoor zruog'
#         >>> g.encrypt('ala ma kota')
#         'dod pd nrwd'
#         >>> g.encrypt('2')
#         Traceback (most recent call last):
#         ...
#         Exception
#         >>> g.encrypt('b')
#         'e'
#         >>> g.encrypt([])
#         Traceback (most recent call last):
#         ...
#         Exception
#         >>> g.encrypt(3.14)
#         Traceback (most recent call last):
#         ...
#         Exception
#         >>> g.encrypt(2)
#         Traceback (most recent call last):
#         ...
#         Exception
#
#
#
#
#         """
#
#
#         cipher = ''
#         if not (isinstance(text, str)):
#             raise Exception
#         for i in text:
#             if i.lower() not in self.alphabet and i != ' ':
#                 raise Exception
#
#             if i.isupper() and i != ' ':
#                 if self.alphabet.index(i.lower()) >= 23:
#                     index = self.alphabet.index(i.lower()) - 23
#                     cipher += (self.alphabet[index]).upper()
#                 else:
#                     index = self.alphabet.index(i.lower()) + 3
#                     cipher += (self.alphabet[index]).upper()
#             elif i.islower() and i != ' ':
#                 if self.alphabet.index(i.lower()) >= 23:
#                     index = self.alphabet.index(i.lower()) - 23
#                     cipher += (self.alphabet[index])
#                 else:
#                     index = self.alphabet.index(i.lower()) + 3
#                     cipher += (self.alphabet[index])
#             else:
#                 cipher += ' '
#         return cipher
#
# if __name__ == "__main__":
#     import doctest
#     import test_ceasar_doctest
#     doctest.testmod(test_ceasar_doctest)