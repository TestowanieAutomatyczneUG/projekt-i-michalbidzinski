class Affine:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    def affine_encrpyt(self, text ,a, b ):
        cipher = ''

        if not (isinstance(text, str)):
            raise Exception
        for i in text:
            if i.lower() not in self.alphabet and i != ' ':
                raise Exception
            if i.isupper() and i != ' ':
                index = ((self.alphabet.index(i.lower()) * a )+ b) % len(self.alphabet)
                cipher += (self.alphabet[index]).upper()
            elif i.islower() and i != ' ':
                index = ((self.alphabet.index(i) * a) + b) % len(self.alphabet)
                cipher += self.alphabet[index]
            else:
                cipher += ' '
        return cipher