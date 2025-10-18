from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.config(bg="#e0f7fa")
root.geometry("700x500")
root.resizable(False, False)

try:
    upload = Image.open("denom.webp")
    upload = upload.resize((250,250))
    image = ImageTk.PhotoImage(upload)
    img_label = Label(root, image=image, bg="#b3e5fc")
    img_label.place(x=225, y=30)
except Exception as e:
    messagebox.showwarning("Image missing!", "Couldnt load image:", e)

title_label = Label(root,text="Denomination counter application", font=("Helvetica", 16, "bold"), bg="#b3e5fc", fg="#2c59d4")
title_label.place(relx=0.5, y=20, anchor=CENTER)


welcome_label = Label(root,text="Hey User, Welcome to the Denomination counter application", font=("Arial", 12, "italic"), bg="#b3e5fc", fg="#2c59d4")
welcome_label.place(relx=0.5, y=320, anchor=CENTER)


entry_label = Label(root,text="Enter Amount", font=("Arial", 12, "bold"), bg="#b3e5fc", fg="#2c59d4")
entry_label.place(relx=0.3, y=370, anchor=CENTER)

amount_entry = Entry(root,font=("Arial", 12), width=15, justify="center")
amount_entry.place(relx=0.55, y=370, anchor=CENTER)

def calculate_denominations():
    try:
        amount = int(amount_entry.get())
        if amount <= 0:
            raise ValueError
        denominations = [1000,500,200,100,50,20,10,5,2,1]
        result = ''
        remaining = amount

        for note in denominations:
            count = remaining//note
            if count>0:
                result+= f"tk {note} x {count} \n"
                remaining %= note
        messagebox.showinfo("Denomination Breakdown", result)

    except ValueError:
        messagebox.showerror("Invalid Input! Please enter a positive amount")


def on_enter(e):
    calc_btn["bg"] = "#0277bd"
def on_leave(e):
    calc_btn["bg"] = "#247eb3"

calc_btn = Button(root,
text='Calculate',
font=("Helvetica", 13, "bold"),
bg="#422eaf",
fg="white",
activebackground="blue",
relief=FLAT,
padx=15,
pady=8,
cursor="hand2",
command=calculate_denominations,
)
calc_btn.place(relx=0.5, y=420, anchor=CENTER)
calc_btn.bind("<Enter>", on_enter)
calc_btn.bind("<Leave>", on_leave)

root.mainloop()