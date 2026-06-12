import random

# 5 predefined words
words = ["python", "coding", "github", "laptop", "program"]

def display_status(guessed_letters, word, wrong_guesses, max_wrong):
    print("\n--- HANGMAN GAME ---")
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Word: {display_word}")
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

def hangman():
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses < max_wrong:
        display_status(guessed_letters, word, wrong_guesses, max_wrong)

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou WIN! The word was: '{word}'")
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only!")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Correct! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word. ({wrong_guesses}/{max_wrong})")

    print(f"\nGame Over! The word was: '{word}'")

def play_again():
    while True:
        hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing!")
            break

play_again()