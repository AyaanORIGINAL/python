from tkinter import *
from datetime import date

window = Tk()
window.title("Sample Window")
window.geometry("400x300")

lbl = Label(window, text = 'Hello world', fg = 'white', bg = 'blue', height = 1, width =250)
name_lbl = Label(text = 'Full name', bg="#0004ff")
name_entry = Entry()
text_box = Text()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! \n Today's date is:" 
    greet = "Hello " + name

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

btn = Button(text='Lets start!', command=display, height=1, bg = '#1261A0', fg = 'white' )


lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()


window.mainloop()