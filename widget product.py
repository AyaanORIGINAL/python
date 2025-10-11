from tkinter import *

window = Tk()
window.title("Product Finder")
window.geometry("400x300")

lbl = Label(window, text="Product Calculator", fg="white", bg="blue", height=2, width=25)
lbl.pack(pady=5)

num1_lbl = Label(window, text="Enter number:", bg="#0004ff", fg="white")
num1_lbl.pack(pady=5)

num1_entry = Entry(window, width=30)
num1_entry.pack(pady=5)

num2_lbl = Label(window, text="Enter another number:", bg="#0004ff", fg="white")
num2_lbl.pack(pady=5)

num2_entry = Entry(window, width=30)
num2_entry.pack(pady=5)

result_box = Text(window, height=3, width=40)
result_box.pack(pady=10)

def display():
    result_box.delete(1.0, END)
    try:
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
        product = num1 * num2
        message = (f"The product of {num1} × {num2} is: {product}")
    except ValueError:
        message = "Please enter valid numbers!"
    result_box.insert(END, message)

btn = Button(window, text="Calculate Product", command=display, height=1, bg="#1261A0", fg="white")
btn.pack(pady=10)

window.mainloop()
