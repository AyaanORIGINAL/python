from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

def convert():
    try:
        inches = float(inch_entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="enter valid number")

Label(root, text="Enter length in inches:").pack(pady=10)
inch_entry = Entry(root)
inch_entry.pack()

Button(root, text="Convert", command=convert).pack(pady=10)
result_label = Label(root, text="")
result_label.pack()

root.mainloop()
