from WordsList import letters
from WordsList import words
import random
import time


def get_word():
    word = random.choice(words)
    return word


def play(word):
    answer = " ".join(word.upper())
    disp = " ".join(word.upper())
    for letter in letters:
        if letter in disp:
            disp = disp.replace(letter, '_')

    stor = [answer, disp]
    return stor


def intro():
    ans = 'yes'
    flag = 0
    while flag == 0:
        answer = input('Ready to Play?\n')
        if ans.upper() in answer.upper():
            time.sleep(0.6)
            print('\nI heard yes :)\n\n')
            flag = 1
            time.sleep(0.6)
        else:
            print('\n'*25)
            time.sleep(2)
            print('\nOk cool. What about now? Are you...')
            time.sleep(0.6)
    game()


def game():
    note = play(get_word())
    answer = note[0]
    board = note[1]
    tries = 6
    while answer != board and tries != 0:
        print('\n'*25 + board + '\nLives:     ' + str(tries))
        guess = input('What is your letter/guess?\n').upper()

        if (len(guess) == 1) and (guess.isalpha()):  # Guess is a letter:
            if guess in answer:
                # Correct Letter:
                board = list(board)  # turning board into indexed list so I can replace
                getRid = findOccurrences(answer, guess)  # finding all indexes to replace

                for index in getRid:
                    board[index] = guess  # replace dashes to letters

                board = ''.join(board)  # turn board back to a string

            else:
                print('\nNot Quite :(')  # Incorrect Letter
                time.sleep(2)
                tries -= 1


        elif len(" ".join(guess)) == len(answer):  # Guess is a word:
            guesscomp = " ".join(guess)
            if guesscomp == answer:  # Guess is correct:
                # change board and guess to a list to replace
                board = list(board)  #
                guesscomp = list(guesscomp)

                for index in range(len(guesscomp)):  # replace all dashes with letters
                    board[index] = guesscomp[index]

                board = "".join(board)

            else:  # Guess is wrong
                print('\nWrong answer :(')
                tries -= 1


        else:
            print('\n Invalid answer lol')
            time.sleep(2)

    if tries == 0:          #Game lost
        print('\n\n\n' + board + '\n'+ answer+ '\nLives:     ' + str(tries))
        print('\nDarn you lost D:\n\n')
        intro()

    elif answer == board:   #Game won
        print('\n\n\n' + board + '\nLives:     ' + str(tries))
        print('\nOMG you won :D\n\n')
        intro()


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


intro()
