from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("800x600")
window.config(bg="#f4f7fc")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

def open_file():
    file_path = askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, "r") as input_file:
        text = input_file.read()
        txt_edit.delete(1.0, END)
        txt_edit.insert(1.0, text)
    window.title(f"Text Editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor - {file_path}")

fr_buttons = Frame(window, relief=RIDGE, bd=3, bg="#07f2cf")
fr_buttons.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

txt_edit = Text(window, wrap=WORD, font=("Consolas", 13), bg="#ffffff", fg="#333", relief=FLAT, padx=10, pady=10)
txt_edit.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

scrollbar = Scrollbar(txt_edit)
scrollbar.pack(side=RIGHT, fill=Y)
txt_edit.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_edit.yview)

def style_button(btn, bg, fg, hover_bg):
    btn.config(
        bg=bg, fg=fg, font=("Helvetica", 12, "bold"),
        relief=FLAT, activebackground=hover_bg, activeforeground="white", cursor="hand2",
        width=15, height=2
    )

btn_open = Button(fr_buttons, text="Open File", command=open_file)
btn_save = Button(fr_buttons, text="Save File", command=save_file)

style_button(btn_open, "#4A90E2", "white", "#357ABD")
style_button(btn_save, "#7ED321", "white", "#6BB61A")

btn_open.pack(fill=X, pady=10)
btn_save.pack(fill=X, pady=10)

footer = Label(window, text="Made with love by Ayaan", bg="#f4f7fc", fg="#888", font=("Arial", 10, "italic"))
footer.grid(row=1, column=0, columnspan=2, pady=5)

window.mainloop()