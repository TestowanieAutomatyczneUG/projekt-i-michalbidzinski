class Morse:
    def __init__(self):
        self.MORSE_CODE = {"\n": "\n", ' ': '   ', 'A': '.-', 'B': '-...',
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
                           "'": ".----.", "@": ".--.-.", ":": "---...",
                           ",": "--..--", "=": "-...-", "!": "-.-.--",
                           "+": ".-.-.", '"': ".-..-.", 'Ą': ".-.-",
                           "Ć": "-.-..", "Ę": "..-..", "Ł": ".-..-",
                           "Ń": "--.--", "Ó": "---.", "Ś": "...-...",
                           }
        self.morse_code_letters = ['', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                                   '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                                   '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....',
                                   '-....',
                                   '--...', '---..', '----.', '--..--', '.-.-.-', '..--..', '-.-.-.', '---...', '-..-.',
                                   ".--.-.", "---...", "--..--", "-...-", "-.-.--", ".-.-.", ".-..-.",
                                   '..--.-', '-.-.--', '-....-', '.-.-.', '-.--.', '-.--.-', '-...-', '.--.-.',
                                   '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', ".-...",
                                   ".----.", ]

    def coding(self, message):
        translation = ''

        for letter in message:
            if letter.upper() in self.MORSE_CODE.keys():
                if letter.upper() != ' ':
                    translation += self.MORSE_CODE[letter.upper()] + ' '
                else:
                    translation += '    '
            else:
                raise Exception
        return translation

    def decoding(self, morse):
        if morse == "":
            raise Exception
        morse_splitted = morse.split(' ')
        if morse_splitted.count('') % 4 != 0:
            raise Exception


        translation = ""
        words = morse.split("   ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                if char not in self.morse_code_letters:
                    raise Exception
                for k, v in self.MORSE_CODE.items():
                    if char == v:
                        translation += k
            translation += " "

        return translation.rstrip()
