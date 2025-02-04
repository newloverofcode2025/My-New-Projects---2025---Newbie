import random

def choose_word():
    # List of words (customize this)
    words = ["sydney", "paris", "rome", "tokyo", "berlin"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Show first letter + blanks/guessed letters
    display = word[0]  # First letter is always visible
    for letter in word[1:]:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word().lower()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6  # Allowed wrong guesses
    first_letter = word[0]
    guessed_letters.add(first_letter)  # Reveal first letter

    print("Welcome to Hangman!")
    print(f"Guess the word: {display_word(word, guessed_letters)}")

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if not guess.isalpha():
            print("Please enter a valid letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            current_display = display_word(word, guessed_letters)
            print(f"Correct! Word: {current_display}")
        else:
            wrong_attempts += 1
            print(f"Wrong! Attempts left: {max_attempts - wrong_attempts}")

        # Check win/lose conditions
        current_display = display_word(word, guessed_letters)  # Update current_display before checking win/lose conditions
        if "_" not in current_display:
            print(f"Congratulations! You won. The word was: {word}")
            break
        elif wrong_attempts >= max_attempts:
            print(f"Game over! The word was: {word}")
            break

if __name__ == "__main__":
    hangman()