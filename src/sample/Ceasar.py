class Ceasar:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
    def encrypt(self, text):
        cipher = ''
        for i in text:
            if i.isupper():
                if self.alphabet.index(i.lower()) >= 23:
                    index = self.alphabet.index(i.lower()) - 3
                    cipher += (self.alphabet[index]).upper()
                else:
                    index = self.alphabet.index(i.lower()) + 3
                    cipher += (self.alphabet[index]).upper()
            else:
                if self.alphabet.index(i.lower()) >= 23:
                    index = self.alphabet.index(i.lower()) - 3
                    cipher += (self.alphabet[index])
                else:
                    index = self.alphabet.index(i.lower()) + 3
                    cipher += (self.alphabet[index])
        return cipher
