import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "fun"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome")
    while attempts > 0:
        display_word = "".join([c if c in guessed_letters else "_" for c in word])
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(c in guessed_letters for c in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Game over! The word was: {word}")

play_hangman()