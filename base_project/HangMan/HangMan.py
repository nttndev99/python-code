import random

# Todo-1: Update the word list to use the 'word_list' from hangmna_words.py
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

# Todo-3: Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    # Todo-4: Update the code below to tell the user how many lives theu have left.
    print(f"**************************** {lives} LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()
    
    # Todo-5: If the user has entered a letter they're already guessed, print the letter and let them know.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    
    # Todo-6: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True

            # Todo-7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        
    # Todo-2: Update the code below to use the stages List from the file hangman_art.py.
    print(stages[lives])



