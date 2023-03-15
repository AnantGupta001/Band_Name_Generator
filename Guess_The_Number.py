# DAY-12
import random
from replit import clear
from art import logo

print(logo)


def game():
    answer = random.randint(1, 100)
    print("Welcome to the Number guessing Game:")
    print("Think of a number between 1 to 100: ")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    def easy():
        attempt = 10
        while attempt != 0:
            print(
                f"You have {attempt} attempts remaining to guess the number.")
            number = int(input("Make a guess: "))

            if number > answer:
                print("Too high.")
                print("Guess again.")
                attempt -= 1

            elif number < answer:
                print("Too Low.")
                print("Guess again.")
                attempt -= 1

            else:
                print(f"You got it! The asnwer was {answer}.")
                break

    def hard():
        attempt = 5
        while attempt != 0:
            print(
                f"You have {attempt} attempts remaining to guess the number.")
            number = int(input("Make a guess: "))

            if number > answer:
                print("Too high.")
                print("Guess again.")
                attempt -= 1

            elif number < answer:
                print("Too Low.")
                print("Guess again.")
                attempt -= 1

            else:
                print(f"You got it! The asnwer was {answer}.")
                break

    if difficulty == 'easy':
        easy()
    else:
        hard()


play = input("Do you want to play this game? Type 'y' or 'n': ")

if play == 'y':
    clear()
    game()
else:
    clear()
