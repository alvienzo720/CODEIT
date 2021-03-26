# import requests

from tkinter import *

from PIL import ImageTk, Image

import json

# App details and configuration

main = Tk()

main.geometry("320x320")

main.title("Hello World")

main.configure(bg="Blue")

img = ImageTk.PhotoImage(Image.open('clouds.png'))

panel = Label(main, image=img)
panel.place(x=112, y=3)


mainloop()
