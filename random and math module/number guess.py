import random

number = random.randint(1,10)
print("Welcome to the number guessing game!")
print("I have selected a Number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    if number == guess:
         print("You have won the game")
         print("The number was", number)
         break
    elif number > guess:
         print("Your guess is less than the number")
    elif guess > number:
         print("Your guess is more than the number")

    else:
         print("Try again")