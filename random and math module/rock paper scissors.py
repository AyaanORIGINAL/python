import random

while True:
    user_action = input("Enter rock, paper, or scissors")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("You chose", user_action, "and the computer chose", computer_action)

    if user_action == computer_action:
        print("You tied the game")
    elif user_action == "rock" and computer_action == "scissors":
        print("You win")
    elif user_action == "paper" and computer_action == "rock":
        print("You win")
    elif user_action == "scissors" and computer_action == "paper":
        print("You win")
    elif user_action == 'rock' and computer_action == "paper":
        print("You lose")
    elif user_action == 'paper' and computer_action == "scissors":
        print("You lose")
    elif user_action == 'scissors' and computer_action == "rock":
        print("You lose")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'n':
        print("Thanks for playing!")
        break
        