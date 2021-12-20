class Ceasar:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    def encrypt(self, text):
        cipher = ''
        if not (isinstance(text, str)):
            raise Exception
        for i in text:
            if i.lower()  not in self.alphabet and i != ' ':
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

