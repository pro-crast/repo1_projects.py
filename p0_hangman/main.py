# importing required modules
import random
import words
import hangman_fig

# main code

choosen_word = random.choice(words.words_database)
# encrypting the word
encrypt_word = []
for letter in range(len(choosen_word)):
    encrypt_word += '_'
print(encrypt_word)

# user input

lives = 6
game_over = False

while not game_over:
    user_letter = input("enter a letter: ")
    #checking user letter with letter in choosen word
    # for letter in choosen_word:
    #     location =0
    #     location = choosen_word.index(letter)
    #     if letter == user_letter:
    #         encrypt_word[location] = letter
    #     location +=1

    # checking user letter with letter in choosen word using index
    for location in range(len(choosen_word)):
        letter = choosen_word[location]
        if letter == user_letter:
            encrypt_word[location] = letter
    print(encrypt_word)

    if user_letter not in choosen_word:
        lives -=1
        print(hangman_fig.hangman[lives])
        if lives == 0:
            print("you loss")
            game_over = True

    #if user_letter in choosen_word:
    if "_" not in encrypt_word:
        print("you won")
        game_over = True