import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Age Calculator App")   
root.geometry("400x400")
root.resizable(False, False)

def calculate_interest():
    try:
        principle = float(principle_var.get())
        time = float(time_var.get())
        rate = float(rate_var.get())

        simple_interest = (principle * rate * time) / 100

        compound_interest = principle * ((1 + rate / 100) ** time) - principle

        
        si_var.set(f"Simple Interest: ${simple_interest:.2f}")
        ci_var.set(f"Compound Interest: ${compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values only!")

ttk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold")).pack(pady=15)

frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Principle ($):", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
principle_var = tk.StringVar()
ttk.Entry(frame, textvariable=principle_var, width=20).grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Time (years):", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_var = tk.StringVar()
ttk.Entry(frame, textvariable=time_var, width=20).grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Rate (%):", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
rate_var = tk.StringVar()
ttk.Entry(frame, textvariable=rate_var, width=20).grid(row=2, column=1, padx=10, pady=5)

ttk.Button(root, text="Calculate", command=calculate_interest).pack(pady=15)

si_var = tk.StringVar()
ci_var = tk.StringVar()
ttk.Label(root, textvariable=si_var, font=("Arial", 12, "bold")).pack(pady=5)
ttk.Label(root, textvariable=ci_var, font=("Arial", 12, "bold")).pack(pady=5)

root.mainloop()
