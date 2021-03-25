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

temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="#9bd7e8")
temp_high_rs = Label(text="Hello", width=20, font=("bold", 20), bg="#9bd7e8")

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="#9bd7e8")
temp_low_rs = Label(text="Hello", width=20, font=("bold", 20), bg="#9bd7e8")
# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="#9bd7e8")
pres_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="#9bd7e8")
hum_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")

# wind
wind = Label(text="Wind Speed :", width=20, font=("bold", 20), bg="#9bd7e8")
wind_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="#9bd7e8")
des_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# country
coun = Label(text="Country :", width=20, font=("bold", 20), bg="#9bd7e8")
coun_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
close_btn = Button(text="Close", bg="Red")

# the grid lay out
title_1.grid(row=0, column=2)
title_2.grid(row=1, column=2)
search_city.grid(row=2, column=2)
button_search.grid(row=2, column=3)
temp_high.grid(row=3, column=2)
temp_high_rs.grid(row=3, column=4)
temp_low.grid(row=4, column=2)
temp_low_rs.grid(row=4, column=4)
pres.grid(row=5, column=2)
pres_rs.grid(row=5, column=4)
hum.grid(row=6, column=2)
hum_rs.grid(row=6, column=4)
wind.grid(row=7, column=2)
wind_rs.grid(row=7, column=4)
desc.grid(row=8, column=2)
des_rs.grid(row=8, column=4)
coun.grid(row=9, column=2)
coun_rs.grid(row=9, column=4)
close_btn.grid(row=20, column=3)

base.mainloop()
