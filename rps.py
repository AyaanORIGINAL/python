import tkinter as tk
import random

def play(user_action):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    result_text = f"You chose {user_action}\nComputer chose {computer_action}\n"

    if user_action == computer_action:
        result_text += "It's a Tie!"
        result_label.config(fg="blue")
    elif user_action == "rock" and computer_action == "scissors":
        result_text += "You Win!"
        result_label.config(fg="green")
    elif user_action == "paper" and computer_action == "rock":
        result_text += "You Win!"
        result_label.config(fg="green")
    elif user_action == "scissors" and computer_action == "paper":
        result_text += "You Win!"
        result_label.config(fg="green")
    else:
        result_text += "You Lose!"
        result_label.config(fg="red")

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#222222")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#222222", fg="white").pack(pady=20)
tk.Label(root, text="Choose your move:", font=("Arial", 13), bg="#222222", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#222222")
frame.pack(pady=10)

tk.Button(frame, text="Rock 🪨", font=("Arial", 12), width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Paper 📄", font=("Arial", 12), width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Scissors ✂️", font=("Arial", 12), width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#222222")
result_label.pack(pady=30)

tk.Button(root, text="Quit", font=("Arial", 12), bg="red", fg="white", width=10, command=root.destroy).pack(pady=10)

root.mainloop()

