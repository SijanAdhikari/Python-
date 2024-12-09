# import art
# import random
# print(art.logo)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# number=random.randint(1,100)
# level=input("Choose a difficulty. Type 'easy' or 'hard': ")
# attempts=0
# if level == "easy":
#     attempts = 10
#     print(f"You have {attempts} attempts remaining to guess the number.")
# elif level == "hard":
#     attempts = 5
#     print(f"You have {attempts} attempts remaining to guess the number.")
#
# def analyze():
#     if play>number:
#         print("Too high.")
#         print("Guess again.")
#         global attempts
#         attempts-=1
#     elif play<number:
#         print("Too low.")
#         print("Guess again.")
#         attempts-=1
#     elif play==number:
#         print(f"You got it! The answer was {number}.")
#
#
#
# guess=True
# while guess:
#     play=int(input("Make a Guess: "))
#     analyze()
#     if play==number:
#         break
#     if attempts==0:
#         print("You've run out of guesses. Refresh the page to run again.")
#         guess=False
#     if play !=number:
#         print(f"You have {attempts} attempts remaining to guess the number.")

from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()


