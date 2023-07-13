from game_settings import max_len_words as maxlw, min_len_words as minlw, gallows_states
from random import randint
DICT = [x.strip() for x in open('source/russian_nouns.txt').readlines() if minlw <= len(x.strip()) <= maxlw]


def createword():
    word = DICT[randint(0, len(DICT)-1)]
    return word, len(word) * '*', len(word)


def open_letters(word, set_with_chars):
    hidden_word = ''
    for i in word:
        if i in set_with_chars:
            hidden_word += i
        else:
            hidden_word += '*'
    return hidden_word


def mistake(count_unknown_letters, hidden_word):
    if count_unknown_letters == hidden_word.count('*'):
        print('You made a mistake :()')
        return True
    else:
        return False


def draw(number_of_mistakes):
    for i in gallows_states[number_of_mistakes]:
        print(i)


def game_end(count_mistakes):
    if count_mistakes == 6:
        print('You lose -_-')
    return not(count_mistakes == 6)


def input_validity(input_str):
    if input_str in ('Y', 'N'):
        return input_str
    else:
        raise Exception("Ошибка ввода, попробуйте ввести 'Y' или 'N'")


def char_is_validity(input_str):
    rus_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)]) + 'ё'
    if len(input_str) == 1 and input_str in rus_alphabet:
        return input_str
    else:
        raise Exception("Ошибка ввода, попробуйте ввести одну строчную букву русского алфавита")


def game_win(count_unknown_letters, word):
    if not count_unknown_letters:
        print(f'You won, take a pie from the shelf! Hidden word was {word}')
    return count_unknown_letters
