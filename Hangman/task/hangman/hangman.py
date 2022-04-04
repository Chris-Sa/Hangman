# Write your code here
import random
import string


def hangman():
    tries = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    wordset = set()
    guessset = set()

    for letter in word:
        wordset.add(letter)

    while tries > 0:

        clue = ""
        for letter in word:
            if letter in guessset:
                clue += letter
            else:
                clue += '-'

        print()
        print(clue)
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue

        if guess not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue

        if guess in guessset:
            print("You've already guessed this letter")
            # print("\n")
            continue

        if guess not in word:
            print("That letter doesn't appear in the word")
            # print("\n")
            tries -= 1

        guessset.add(guess)

        if wordset.intersection(guessset) == wordset:
            print(word)
            break

    if wordset.intersection(guessset) == wordset:
        print("You guessed the word {}!".format(word))
        print("You survived!")

    else:
        print("You lost!")

    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        hangman()


print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit:')


if menu == "play":
    hangman()