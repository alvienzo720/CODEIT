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


'''start our fields and labels which will be displaying
the data'''
# title labels
title_1 = Label(text="Weather App", width=20, font=("bold", 20), bg="#9bd7e8")

title_2 = Label(text="Search for Weather of any city of your choice", width=32, font=("italics", 15), bg="#9bd7e8")
# Search feild and button in grid format

search_city = tk.Entry(text="Search for city")
button_search = tk.Button(text="Search", bg="white")

# temp output and label

