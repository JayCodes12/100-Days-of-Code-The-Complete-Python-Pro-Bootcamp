import random
import hangman_words
import hangman_art


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(hangman_art)

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    if lives == 6:
        print("********************************6/6 LIVES LEFT****************************")
    elif lives == 5:
        print("********************************5/6 LIVES LEFT****************************")
    elif lives == 4:
        print("********************************4/6 LIVES LEFT****************************")
    elif lives == 3:
        print("********************************3/6 LIVES LEFT****************************")
    elif lives == 2:
        print("********************************2/6 LIVES LEFT****************************")
    elif lives == 1:
        print("********************************1/6 LIVES LEFT****************************")
    else:
        print("***********************************Game Over****************************")

    guess = input("Guess a letter: ").lower()
    guessed_letters = [guess]
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
   # if guess == guess:
        #print(f"You've already guessed {guess}")

    if guess in chosen_word or guess not in chosen_word:
        print(f"{guess}\n")
        guessed_letters.append(guess)

    elif guess == guessed_letters:
        #print(guessed_letters)
        print(f"You've already guessed {guessed_letters}")
    else:
        continue
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

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
        print(hangman_art.stages)
