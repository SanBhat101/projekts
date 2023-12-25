# Morse code translator

#import logging
from typing import Dict, List, Tuple
import  re

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
    ' ':' ',
}

MORSE_TO_ENG_DICT: Dict[str, str] = {v: k for k, v in ENG_TO_MORSE_DICT.items()}

# user input
#user_string: List[str] =input("Please enter the string to be translated: ")
user_string="abc $ def & ghi x test { kampai { }"


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


def morse_to_e(text: str) -> str:
    translate_txt=""
    eng_txt=""
    s_c=0

    for chr in text:
        if chr !=" ":
            translate_txt+=chr
            s_c=0
            continue
        if chr == " " or chr == "\n":
            s_c+=1
            if s_c>1:
                eng_txt+=" "
            else:
                eng_txt+=MORSE_TO_ENG_DICT[translate_txt]
                #print(eng_txt)
                translate_txt=""
            #print(eng_txt)
    if translate_txt:
        eng_txt+=MORSE_TO_ENG_DICT[translate_txt]

    return eng_txt

def morse_to_eng(text: str) -> str:
    translate_txt = ""
    eng_txt = ""
    invalid_chars=[]

    words = re.split(r"\s{2,}", text) # split on 2 or more spaces

    for word in words:
        letters = word.split(" ")

        for letter in letters:
            try:
                if letter != "":
                    translate_txt += letter
                    eng_txt += MORSE_TO_ENG_DICT[translate_txt]
                    translate_txt = ""
            except:
                invalid_chars.append(letter)
                eng_txt += "?"
        
        eng_txt += " "
    
    return eng_txt.strip(),invalid_chars


#output
if __name__ == '__main__':
    user_string=translate_to_morse(user_string)
    print(user_string[0])
    print("Sorry, could not process characters in order: ", end='') 
    for i in user_string[1]:
        print(i, end=' ')
    print()
    print(morse_to_eng(".-  -... -.-.    ...-..-    -.. . ..-.    .-...  --. .... ..  -..-  - . ... -  {"))


