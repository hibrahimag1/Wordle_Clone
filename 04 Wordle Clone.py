from random import choice
from wordlist import words
from collections import Counter
import colorama
import sys
from os import system, name


def main():
    # clear terminal screen function
    def clear():  
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

    clear()
    play_again = True
    while play_again:
        CURSOR_UP_ONE = '\x1b[1A' 
        ERASE_LINE = '\x1b[2K'

        def delete_last_line():
            sys.stdout.write(CURSOR_UP_ONE) 
            sys.stdout.write(ERASE_LINE)

        def color_letter(word):
            for letter in word:
                if letter[0] == "-":
                    print(f'{colorama.Fore.LIGHTGREEN_EX}{letter[-1].upper()}{colorama.Style.RESET_ALL}', end=" ")
                elif letter[0] == ".":
                    print(f'{colorama.Fore.YELLOW}{letter[-1].upper()}{colorama.Style.RESET_ALL}', end=" ")
                else:
                    print(f'{colorama.Style.DIM}{letter.upper()}{colorama.Style.RESET_ALL}', end=" ")

        answer = choice(words)
        guesses = 6

        print("_ _ _ _ _")

        while guesses > 0:

            letter_counter = Counter(answer)
            word = []

            # validate input
            player_input = input()
            while player_input not in words or len(player_input) != 5:
                delete_last_line()
                player_input = input()
            if guesses == 6:
                delete_last_line()
            delete_last_line()

            # check for letters in right positions
            for index, letter in enumerate(player_input):
                if letter == answer[index]:
                    word.append(f"-{letter}")  # added the '-' so we can identify and color it later
                    letter_counter[letter] -= 1
                else:
                    word.append("_")

            # check for letters in bad positions, and wrong letters
            for index, letter in enumerate(player_input):
                if letter != answer[index] and letter_counter[letter] > 0:
                    word[index] = f".{player_input[index]}" # added the '.' so we can identify and color it later
                    letter_counter[letter] -= 1
                elif (word[index] == "_" and letter_counter[letter] == 0):
                    word[index] = letter

            # print word by letter
            color_letter(word)

            # continue the game unless player won
            if player_input == answer:
                print()
                print(f"You won! The word is {answer}!")
                break
            else:
                guesses -= 1
                print()

        # in case all guesses were used and lose
        if player_input!=answer:
            print(f"The word was {answer.upper()}. Better luck next time.")

        play_again = input("Want to play again? (Y/N) ")
        if play_again[0].lower() !="y":
            play_again = False
        clear()

if __name__ == "__main__":
    main()