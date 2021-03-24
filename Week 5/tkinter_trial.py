import tkinter as tk
from tkinter import *


root = tk.Tk()

root.title("UI WITH TKINTER")


def hello():
    te = text_entry.get()
    output_textbox.insert(INSERT, te)
    output_textbox.pack()
    print("button clicked")


button = tk.Button(text="Click", command=hello)

button.pack()

text_entry = tk.Entry()
text_entry.pack()

output_textbox = tk.Text()


output_textbox.pack()

root.mainloop()
