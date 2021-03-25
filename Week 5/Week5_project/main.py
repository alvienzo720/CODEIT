from tkinter import *
import tkinter as tk
# import tinker as a whole and after import tkinter as tk

base = Tk()

# we configure our app title and dimensions and background colour
base.title("Weather App")
base.configure(bg="#9bd7e8")
base.geometry("480x480")
# configure our rows and columns
base.rowconfigure(0, minsize=50)
base.columnconfigure([0, 1, 2], minsize=2)


