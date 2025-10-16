from tkinter import *

root = Tk()
root.title("Paint App")
root.geometry("600x400")

canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=True)

last_x, last_y = None, None

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill='black', width=3)
    last_x, last_y = event.x, event.y

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def stop_draw(event):
    global last_x, last_y
    last_x, last_y = None, None

def clear_canvas(event):
    canvas.delete("all")

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

root.bind("<c>", clear_canvas)

label = Label(root, text='Click and drag to draw. Press "c" to clear.')
font=('Arial', 12)
label.pack(pady=5)

root.mainloop()
