# Task-1
# CodeAlpha
# create simple text-based Hangman game where the player guesses a word one letter at a time.
# Simplified Scope:
# ● Use a small list of 5 predefined words (no need to use a file or API).
# ● Limit incorrect guesses to 6.
# ● Basic console input/output — no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.

import random

words = ["apple", "tiger", "pizza", "snake", "chair"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6

print("Welcome to Hangman!")
print("Guess the word. You have 6 chances.\n")

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    letter = input("Enter a letter: ").lower()

    if letter in word:
        new_guessed = ""
        for i in range(len(word)):
            if word[i] == letter:
                new_guessed += letter
            else:
                new_guessed += guessed[i]
        guessed = new_guessed
        print("Correct!\n")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts, "\n")

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("You lose! The word was:", word)
