import random

class Fruitquiz:
    def __init__(self):
        self.fruits = {"apple": "red",
                       "banana": "yellow",
                       "grape": "purple",
                       "watermelon": "green",
                       "orange": "orange",
                       }
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}?")
            user_ans = input()
            if user_ans.lower() == color:
                print("Correct!")
            else:
                print("Wrong!")
            option = int(input("Do you want to continue? 0 if yes, 1 if no: "))
            if option == 1:
                break

print("Welcome to fruit quiz")
fq = Fruitquiz()
fq.quiz()