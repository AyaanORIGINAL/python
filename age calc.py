from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator")
root.geometry("400x400")

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))

    result_label.config(text=f"Your age is {age} years")

Label(root, text="Enter Day:").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Enter Month:").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Enter Year:").pack()
year_entry = Entry(root)
year_entry.pack()

Button(root, text="Calculate Age", command=calculate_age).pack(pady=5)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()