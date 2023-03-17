# DAY-14
import random
import art
from game_data import data
from replit import clear

print(art.logo)

account_b = random.choice(data)
score = 0
game_should_continue = True

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    def format_data(account):
        """Takes the account data and returns in printable format."""
        account_name = account['name']
        account_description = account['description']
        account_country = account['country']
        return f"{account_name}, a {account_description}, from {account_country}"


    def check_answer(guess, a_followers, b_followers):
        """Takes the user's guess and follower counts and returns if they got it right."""
        if a_followers > b_followers:
            return guess == 'a'
        else:
            return guess == 'b'


    print(f"Compare A: {format_data(account_a)}.")

    print(art.vs)

    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(art.logo)

    if is_correct:
        score += 1
        print(f"You got it! Current Score {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score {score}")
