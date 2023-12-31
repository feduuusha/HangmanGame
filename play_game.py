from game_engine import *

game_is_run = 0
while True:
    if not game_is_run:
        print('Do you like to play? [Y]es or [N]o')
        if input_validity(input()) == 'Y':
            game_is_run = 1
            set_with_char = set()
            word, hidden_word, count_unknown_letters = createword()
            count_mistakes = 0
            draw(count_mistakes)
        else:
            print('Ok bay-bay, see you later!')
            break

    print(f'You word is {hidden_word}, number of mistakes: {count_mistakes}\nChose you char:')
    set_with_char.add(char_is_validity(input()))
    hidden_word = open_letters(word, set_with_char)
    # Так как функция mistake возращает True в случае ошибки и False в случае успеха, то так можно считать кол-во ошибок
    count_mistakes += mistake(count_unknown_letters, hidden_word)
    count_unknown_letters = hidden_word.count('*')
    draw(count_mistakes)
    ''' В этом случае функция min используется для одновременного присвоения меньшего из значений функции
        game_win и game_end, игра продолжается до того момента, пока одна из функция не вернёт ноль'''
    game_is_run = min(game_lose(count_mistakes), game_win(count_unknown_letters, word))
