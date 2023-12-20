# Morse code translator

# eng to morse dict
to_morse ={
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
    #special chars
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

}


# user input
#usr_str=input("Please enter the string to be translated: ")
usr_str="abc $ def & ghi * test { kampai"


#translate func
def translate(text):
    text=text.upper()
    morse_str=""
    invalid_chars=""
    for chr in text:
        try:
            if chr == " ":
                morse_str+="  "
            else:
                morse_str+=to_morse[chr]+" "
        except:
            invalid_chars+=chr+" "
    print("Sorry, could not process Characters: "+invalid_chars)
    return morse_str


#output
print(translate(usr_str))