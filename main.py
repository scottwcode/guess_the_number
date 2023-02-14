# This Number Guessing Game Has the following rules:
#   A number is chosen between 1-100 that the player should try to guess
#   The player guesses a number between 1-100
#   Hints are given with each guess of "Too high." or "Too low."
#   The player will have a finite number of guesses based on difficulty level
#   The player will choose a difficulty level before guessing starts:
#           Easy - 10 guesses
#           Hard - 5 guesses
from random import randint
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

# get_attempts gets the number of attempts the user has to guess the
# number based on difficulty.


def get_attempts():
    need_difficulty = True
    while need_difficulty:
        diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if diff == "easy":
            return EASY_ATTEMPTS
        elif diff == "hard":
            return HARD_ATTEMPTS
        else:
            print(f"{diff} is not a valid difficulty.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = get_attempts()
    answer = randint(1, 100)
    while attempts >= 0:
        if attempts == 0:
            print(
                f"You've run out of attempts :-( The number was {answer}. Better luck next time.")
            break
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            break
        elif guess < answer:
            print("Too low.")
            attempts -= 1
        else:
            print("Too high.")
            attempts -= 1


game()
