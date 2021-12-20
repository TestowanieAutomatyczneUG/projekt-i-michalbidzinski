class Affine:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    def affine_encrpyt(self, text ,a, b ):
        cipher = ''
        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise Exception

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

    def affine_decrpyt(self, text ,a, b ):
        def egcd(a, b):
            x, y, u, v = 0, 1, 1, 0
            while a != 0:
                q, r = b // a, b % a
                m, n = x - u * q, y - v * q
                b, a, x, y, u, v = a, r, u, v, m, n
            gcd = b
            return gcd, x, y

        def modinv(a, m):
            gcd, x, y = egcd(a, m)
            if gcd != 1:
                return None
            else:
                return x % m
        a_inv = modinv(a, len(self.alphabet))
        decrypted_message = ''
        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise Exception

        if not (isinstance(text, str)):
            raise Exception
        for i in text:
            if i.lower() not in self.alphabet and i != ' ':
                raise Exception
            if i.isupper() and i != ' ':
                index =  (a_inv  * (self.alphabet.index(i.lower()) - b)) % len(self.alphabet)
                decrypted_message += (self.alphabet[index]).upper()
            elif i.islower() and i != ' ':
                index = (a_inv  * (self.alphabet.index(i) - b)) % len(self.alphabet)
                decrypted_message += (self.alphabet[index])
            else:
                decrypted_message += ' '
        return decrypted_message