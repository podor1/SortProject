import re

RUSSIAN_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "jo", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ji", "", "a" , "ju", "ja")

TRANS = {}

for key, value in zip(RUSSIAN_SYMBOLS, TRANSLATION) :
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()

def normalize(name) :
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W','_', new_name)
    return f"{new_name}.{'.'.join(extension)}"

