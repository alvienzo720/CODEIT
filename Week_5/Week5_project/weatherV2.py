from tkinter import *
import tkinter as tk
import tkinter.messagebox
import requests
# from tkinter import Label, Menu, StringVar
# from tkinter import Tk
from PIL import ImageTk, Image

tk = Tk()
base = tk
base.title("Group 6 Weather App")
base.config(bg="blue")
base.geometry("400x600")

img = Image.open("/Users/moseswagabaza/PycharmProjects/Weather_App/weather.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)


# # Search field and button in grid format
# city_name = StringVar()
search_city = Entry(text="Search for city").grid(row=3, column=3)

#
# def search_weather():
#     api_key = "14ed2a78adcbcbfe1ac9d1ffb8c5eea6"
#
#     base_url = "https://api.openweathermap.org/data/2.5/weather?"
#
#     city_names = search_city.get()
#
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_names
#
#     # response
#
#     response = requests.get(complete_url)
#
#     x = response.json()
#
#     try:
#         if ['cod'] != '400':
#             y = x['main']
#             temp_High = round(y['temp_max'] - 273.15)
#             temp_Low = round(y['temp_min'] - 273.15)
#             pressure_value = y['pressure']
#             hum_value = y['humidity']
#
#         z = x['weather']
#         description_weather = z[0]['description']
#
#         m = x['sys']
#         country_detail = m['country']
#
#         temp_high_rs.configure(text=temp_High)
#         temp_low_rs.configure(text=temp_Low)
#         pres_rs.configure(text=pressure_value)
#         hum_rs.configure(text=hum_value)
#         des_rs.configure(text=description_weather)
#         coun_rs.configure(text=country_detail)
#     except:
#         tkinter.messagebox.showinfo("Error", "City not found")
#
#
# button_search = tk.Button(text="Search", bg="white", command=search_weather)
#

# function for closing app via menu


def close_app():
    closeapp = tkinter.messagebox.askyesno("Group 6 Weather App", "Do you want to exit App?")
    if closeapp > 0:
        base.destroy()
        return


# additional function for displaying credits in menu


def credits_func():
    credits_func = tkinter.messagebox.showinfo(title="Credits", message='''Made with love by Group 6 CIT TIV
***Mohammed
***Alvin
***Hassan
***Moses
***Francis
GPL V4 License 2021''')
    return


# tkinter gui formatting

# menu bars
menubar = Menu(base)
base.configure(menu=menubar)
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=credits_func)

# temp output and label
temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="blue").grid(row=4, column=0)
temp_high_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=4, column=2)

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="blue").grid(row=5, column=0)
temp_low_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=5, column=2)
# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="blue").grid(row=6, column=0)
pres_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=4, column=2)
# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="blue").grid(row=7, column=0)
hum_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=4, column=2)

# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="blue").grid(row=8, column=0)
des_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=8, column=2)
# country

coun = Label(text="Country :", width=20, font=("bold", 20), bg="blue").grid(row=9, column=0)
coun_rs = Label(text="", width=20, font=("bold", 20), bg="blue").grid(row=9, column=2)

footer_1 = Label(text="Temperature is measured in Degrees Celsius").grid(row=10, column=3)
footer_2 = Label(text="Pressure in Pascals (Pa)").grid(row=11, column=3)
footer_3 = Label(text="Humidity is measured in grams Per Kilogram of air(g/Kg)").grid(row=12, column=3)

base.mainloop()
