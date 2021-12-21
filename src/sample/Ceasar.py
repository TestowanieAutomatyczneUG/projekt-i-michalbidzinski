class Ceasar:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    def encrypt(self, text):
        """
             >>> g = Ceasar()
             >>> g.encrypt('a')
             'd'
             >>> g.encrypt('VENI')
             'YHQL'
             >>> g.encrypt('XYZ')
             'ABC'
             >>> g.encrypt('xyz')
             'abc'
             >>> g.encrypt('abcdefghijklmnopqrstuvxyz')
             'defghijklmnopqrstuvwxyabc'

             >>> g.encrypt('hello world')
             'khoor zruog'
             >>> g.encrypt('ala ma kota')
             'dod pd nrwd'
             >>> g.encrypt('2')
             Traceback (most recent call last):
             ...
             Exception
             >>> g.encrypt('b')
             'e'
             >>> g.encrypt([])
             Traceback (most recent call last):
             ...
             Exception
             >>> g.encrypt(3.14)
             Traceback (most recent call last):
             ...
             Exception
             >>> g.encrypt(2)
             Traceback (most recent call last):
             ...
             Exception




             """
        cipher = ''
        if not (isinstance(text, str)):
            raise Exception
        for i in text:
            if i.lower() not in self.alphabet and i != ' ':
                raise Exception

            if i.isupper() and i != ' ':
                if self.alphabet.index(i.lower()) >= 23:
                    index = self.alphabet.index(i.lower()) - 23
                    cipher += (self.alphabet[index]).upper()
                else:
                    index = self.alphabet.index(i.lower()) + 3
                    cipher += (self.alphabet[index]).upper()
            elif i.islower() and i != ' ':
                if self.alphabet.index(i.lower()) >= 23:
                    index = self.alphabet.index(i.lower()) - 23
                    cipher += (self.alphabet[index])
                else:
                    index = self.alphabet.index(i.lower()) + 3
                    cipher += (self.alphabet[index])
            else:
                cipher += ' '
        return cipher

    def decrypt(self, text):
        """
                    >>> g = Ceasar()
                    >>> g.decrypt('a')
                    'x'
                    >>> g.decrypt('VENI')
                    'SBKF'
                    >>> g.decrypt('XYZ')
                    'UVW'

                    >>> g.decrypt('abcdefghijklmnopqrstuvxyz')
                    'xyzabcdefghijklmnopqrsuvw'

                    >>> g.decrypt('hello world')
                    'ebiil tloia'
                    >>> g.decrypt('ala ma kota')
                    'xix jx hlqx'
                    >>> g.decrypt('2')
                    Traceback (most recent call last):
                    ...
                    Exception
                    >>> g.decrypt('b')
                    'y'
                    >>> g.decrypt([])
                    Traceback (most recent call last):
                    ...
                    Exception
                    >>> g.decrypt(3.14)
                    Traceback (most recent call last):
                    ...
                    Exception
                    >>> g.decrypt(2)
                    Traceback (most recent call last):
                    ...
                    Exception

                    """
        decrypted_text = ''
        if not (isinstance(text, str)):
            raise Exception

        for i in text:
            if i.lower() not in self.alphabet and i != ' ':
                raise Exception

            if i.isupper() and i != ' ':
                if self.alphabet.index(i.lower()) <= 2:
                    index = self.alphabet.index(i.lower()) + 23
                    decrypted_text += (self.alphabet[index]).upper()
                else:
                    index = self.alphabet.index(i.lower()) - 3
                    decrypted_text += (self.alphabet[index]).upper()
            elif i.islower() and i != ' ':
                if self.alphabet.index(i.lower()) <= 2:
                    index = self.alphabet.index(i.lower()) + 23
                    decrypted_text += (self.alphabet[index])
                else:
                    index = self.alphabet.index(i.lower()) - 3
                    decrypted_text += (self.alphabet[index])
            else:
                decrypted_text += ' '
        return decrypted_text
