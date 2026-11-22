# Creativity: The game chooses a random secret word from a list of Book of Mormon names and terms,
# making the game different each time it is played.

import random

print("Welcome to the word guessing game!\n")

# List of possible secret words
words = ["mosiah", "nephi", "moroni", "alma", "helaman", "temple"]
secret_word = random.choice(words)

guess_count = 0

# Generate initial hint
hint = ""
for _ in secret_word:
    hint += "_ "

print(f"Your hint is: {hint}")

guess = ""

while guess.lower() != secret_word:
    guess = input("What is your guess? ")
    guess_count += 1
    if guess.lower() == secret_word:
        print("Congratulations! You guessed it!")
        break

    # Check word length
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue

    # Generate hint
    hint = ""

    for i in range(len(secret_word)):
        guess_letter = guess[i]
        secret_letter = secret_word[i]

        # Correct letter in correct position
        if guess_letter.lower() == secret_letter.lower():
            hint += guess_letter.upper() + " "

        # Letter exists in secret word but wrong position
        elif guess_letter.lower() in secret_word.lower():
            hint += guess_letter.lower() + " "

        # Letter not in secret word
        else:
            hint += "_ "

    print(f"Your hint is: {hint}")

print(f"It took you {guess_count} guesses.")
