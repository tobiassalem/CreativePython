import random

user_score = 0
computer_score = 0
possible_actions = ["rock", "paper", "scissors"]


def print_score():
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

while True:
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1

    print_score()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f"Ok bye! ^^ ")
        break
    else:
        print(f"Ok cool, let's go again!")



