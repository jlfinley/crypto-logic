import random


# --------------Creating the word-------------- #
f = open("wordlist.txt")
words = f.readlines()
f.close()
wordRandom = random.choice(words).upper()
wordRandom = wordRandom.replace("\n", "")
wordLetters = list(wordRandom)
wordScramble = random.shuffle(wordLetters)
# --------------------------------------------- #


# ------------------The Game------------------- #
def intro():
    print("Welcome to CRYPTO-LOGIC!")
    print("Try to guess the scrambled word, one letter at a time!")


def game():
    global bad_guess
    bad_guess = 0
    index = 0
    global wordAnswer
    wordAnswer = ""
    while index < len(wordRandom):
        print("Incorrect Guesses:", bad_guess)
        print(''.join(wordLetters))
        print(wordAnswer)
        answer = input("Your guess?  ")
        answer = answer.upper()
        if answer != wordRandom[index]:
            bad_guess += 1

        elif answer == wordRandom[index]:
            wordAnswer += answer
            index += 1

# ---------------------------------------------- #


# ----- #

intro()
game()

# ----- #
print(wordAnswer)
print("")
print("Congratulations! You guessed the word after only", bad_guess, "incorrect guess(es)!")
input("Press ENTER to exit:  ")

