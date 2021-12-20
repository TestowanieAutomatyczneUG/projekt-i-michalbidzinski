class Affine:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    def affine_encrpyt(self, text ,a, b ):
        cipher = ''
        for i in text:
            if i.isupper():
                index = ((self.alphabet.index(i.lower()) * a )+ b) % len(self.alphabet)
                cipher += (self.alphabet[index]).upper()
            else:
                index = ((self.alphabet.index(i) * a) + b) % len(self.alphabet)
                cipher += self.alphabet[index]
        return cipher