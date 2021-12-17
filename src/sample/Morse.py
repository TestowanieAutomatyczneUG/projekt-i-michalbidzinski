class Morse:
    def __init__(self):
        self.MORSE_CODE = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', "&": ".-...",
                      "'": ".----.",
                      "@": ".--.-.",
                      ":": "---...",
                      ",": "--..--",
                      "=": "-...-",
                      "!": "-.-.--",
                      "+": ".-.-.",
                      '"': ".-..-.",
                      'Ą': ".-.-",
                      "Ć": "-.-..",
                      "Ę": "..-..",
                      "Ł": ".-..-",
                      "Ń": "--.--",
                      "Ó": "---.",
                      "Ś": "...-..."

                      }

    def coding(self, message):
        translation = ''

        for letter in message.replace(" ", ""):
            if letter.upper() in self.MORSE_CODE.keys():
                if letter.upper() != ' ':
                    translation += self.MORSE_CODE[letter.upper()] + ' '
                else:
                    translation += ' '
            else:
                raise Exception


        return translation

    def decoding(self, morse):

        if morse == "":
            raise Exception("Wprowadz kod morse")
        if "    " in morse:
            raise Exception("Za dużo spacji")
        translation = ""
        words = morse.split("   ")
        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.MORSE_CODE.items():
                    if char == v:
                        translation += k
            translation += " "

        return translation.rstrip()
