
import tkinter as tk

root = tk.Tk()

root.title("UI WITH TKINTER")


def hello():
    te = text_entry.get()
    print("button clicked")


button = tk.Button(text="Click", command=hello)

button.pack()

text_entry = tk.Text()
text_entry.pack()

output_textbox = tk.Text()

output_textbox.pack()

root.mainloop()
