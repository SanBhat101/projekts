# Morse code translator

#import logging
from typing import Dict, List, Tuple

# English to Morse Code mapping dictionary
ENG_TO_MORSE_DICT: Dict[str, str] = {
    # alphabet
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
    # numbers
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
    # special chars
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    '`':'.----.',
    '/':'-..-.',
    '(':'-.--.',
    ')':'-.--.-',
    ':':'---...',
    '=':'-...-',
    '+':'.-.-.',
    '-':'-....-',
    '"':'.-..-.',
    '@':'.--.-.',
    '$':'...-..-', # not in international
    '_':'..--.-',
    ';':'-.-.-.',
    '&':'.-...',   # not in international
    '!':'-.-.--',  # not in international
    '*':'-..-',
    '×':'-..-',
    ' ':' ',
}


# user input
#user_string: List[str] =input("Please enter the string to be translated: ")
user_string="abc $ def & ghi * test { kampai { }"


# translate function
#extended translate with error handling
def translate_to_morse(text: str) -> str:
    text=text.upper()
    morse_code=""
    invalid_chars=[]
    for chr in text:
        try:
            morse_code+=ENG_TO_MORSE_DICT[chr]+" "
        except:
            #invalid_chars+=chr+" "
            invalid_chars.append(chr)
            morse_code+="? "

    return morse_code,invalid_chars


#output
if __name__ == '__main__':
    user_string=translate_to_morse(user_string)
    print(user_string[0])
    print("Sorry, could not process characters in order: ", end='') 
    for i in user_string[1]:
        print(i, end=' ')


