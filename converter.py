import pyperclip
import time
from winapi import get_definition
import re
import string
import os
import keyboard
from threading import Thread
import beepy
from playsound import playsound


rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', ';', '<', '>']

rus_to_eng_keyboard = {
    'ё': '`', 'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y',
    'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a',
    'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k',
    'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v',
    'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'Ё': '~', 'Й': 'Q',
    'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I',
    'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', 'Ф': 'A', 'Ы': 'S', 'В': 'D',
    'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':',
    'Э': '"', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N',
    'Ь': 'M', 'Б': '<', 'Ю': '>', ',': ',', '.': '.', '/': '/', 'Ё': '~',
    'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
    'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', 'Ф': 'A', 'Ы': 'S',
    'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L',
    'Ж': ':', 'Э': '"', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B',
    'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>'
};

eng_to_rus_keyboard = {
    '`': 'ё', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
    'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф',
    's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
    'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м',
    'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '~': 'Ё',
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
    'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы',
    'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
    ';': 'Ж', "'": 'Э', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И',
    'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю'
};

ActiveApp = False

def switch_keyboard_layout(layout_id):
    # Использование AppleScript для смены раскладки на macOS
    script = f'''
    tell application "System Events"
        set current_layout to (name of current input source)
        if current_layout is not "{layout_id}" then
            do shell script "osascript -e 'tell application \"System Events\" to keystroke space using {{command down}}'"
        end if
    end tell
    '''
    os.system(f"osascript -e '{script}'")

def check_english(word):
    return lambda word: bool(re.match("^[a-zA-Z]+$", word))

def analyzer(text):
    #total_letters = len(text)
    english_letters = sum(1 for char in text if char.isalpha() and char.isascii())
    russian_letters = sum(1 for char in text if char.isalpha() and not char.isascii())

    if english_letters > russian_letters:
        return 'en'
    elif russian_letters > english_letters:
        return 'ru'
    else:
        return 'en'

def translate_to_rus(text):
    conversion_text = ""
    read_string_split = text.split()
    for word in read_string_split:
        punctuation = ''
        while word and word[-1] in string.punctuation and word[-1] not in '. , ; \'':
            punctuation = word[-1] + punctuation
            word = word[:-1]
        if word != '':
            if get_definition(word.lower()) and len(word) > 1:
                conversion_text += word + punctuation + " "
            else:
                for char in word:
                    if char.lower() in eng_alphabet:
                        conversion_text += eng_to_rus_keyboard[char]
                    else:
                        conversion_text += char
                conversion_text += punctuation + " "
    #switch_keyboard_layout('com.apple.keylayout.Russian')
    return conversion_text

def translate_to_eng(text):
    conversion_text = ""
    read_string_split = text.split()
    for word in read_string_split:
        punctuation = ''
        while word and word[-1] in string.punctuation and word[-1] not in '. ; \'':
            punctuation = word[-1] + punctuation
            word = word[:-1]
        if word != '':
            if get_definition(word.lower()) and len(word) > 1:
                conversion_text += word + punctuation + " "
            else:
                for char in word:
                    if char.lower() in rus_alphabet:
                        conversion_text += rus_to_eng_keyboard[char]
                    else:
                        conversion_text += char
                conversion_text += punctuation + " "

    #switch_keyboard_layout('com.apple.keylayout.US')
    return conversion_text

def scanner(read_string):
    conversion_text = ''
    result = analyzer(read_string)

    if result == 'ru':
        conversion_text = translate_to_eng(read_string)
    else:
        conversion_text = translate_to_rus(read_string)
    return conversion_text

def load_abbreviations_func():
    key, values = [], []
    if os.path.exists("abbreviations.txt"):
        with open("abbreviations.txt", "r") as file:
            for line in file:
                line = line.split()
                key.append(line[0])
                values.append(' '.join(line[1:]))
            abbreviations = dict(zip(key, values))
    return abbreviations


def get_abbreviations(text, abbreviations):
    return abbreviations.get(text)


def start_program():
    global ActiveApp
    ActiveApp = True
    pyperclip.copy('')
    #thread = Thread(target=handler, args=(lambda: ActiveApp,))
    #thread = Thread(target=handler)
    #thread.start()
    handler(ActiveApp)


def stop_program():
    global ActiveApp
    ActiveApp = False
    pyperclip.copy('')


def play_signal():
    beepy.beep(sound='coin')


def handler(flag):
    abbreviations = load_abbreviations_func()
    print("cловарь сокращений загружен")
    converter_string = ""
    while converter_string == "":
        copy_text = pyperclip.paste()
        if copy_text != '' or copy_text == None:
            autocorrect = get_abbreviations(copy_text.lower().rstrip(), abbreviations)
            if autocorrect != None:
                pyperclip.copy(autocorrect)
                playsound('e4fd05103e0d514.mp3')
                break
            if converter_string != copy_text:
                print(copy_text)
                converter_string = scanner(copy_text.rstrip())
                pyperclip.copy(converter_string)
                playsound('e4fd05103e0d514.mp3')
            else:
                #time.sleep(1)
                pyperclip.copy('')
        else:
            time.sleep(1)
#pyperclip.copy('')
#start_program()