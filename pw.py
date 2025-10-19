import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.resizable(False, False)

def check_strength(*args):
    password = password_var.get()
    length = len(password)

    if length == 0:
        strength_label.config(text="Enter a password", foreground="black")
    elif length <= 5:
        strength_label.config(text="Weak", foreground="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", foreground="orange")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", foreground="lightgreen")
    else:
        strength_label.config(text="Very Strong", foreground="darkgreen")


title_label = ttk.Label(root, text="🔒 Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=20)

password_var = tk.StringVar()
password_var.trace("w", check_strength)  

entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

ttk.Label(entry_frame, text="Enter Password: ", font=("Arial", 11)).grid(row=0, column=0, padx=5)
password_entry = ttk.Entry(entry_frame, textvariable=password_var, show="*", width=25, font=("Arial", 11))
password_entry.grid(row=0, column=1, padx=5)

strength_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=20)

root.mainloop()
