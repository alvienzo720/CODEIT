# from tkinter import *
# import tkinter as tk
# Create a dictionary that prints out keys and values.

# cities = {1: 'jinja', 2: 'Kampala', 3: 'Gulu', 4: 'Entebbe'}
#
# for city in cities:
#     print(city, ' ', cities[city])

# # Create a class function of your top 3 Music Artist.

# # Create a for loop that only prints out even numbers.

# num = 100

# for num in range(100):
#     if num % 2 == 0:
#         print(num)

# # Create a while loop that only prints out odd numbers.
# num = 1
# while num < 100:
#     if num % 2 == 1:
#         print(num)
#     num += 1

# # Create a variable that only prints out the first letter of your name.

# my_name = "Alvin"

# first_letter_of_my_name = my_name[0]

# print(first_letter_of_my_name)

# # Create a list that only prints out 2 items in the list.

# cars = ['Toyota', 'Mazda', 'RangeRover', 'BMW', 'RollsRoyce']

# print(cars[2:4])

# Create a Tkinter program that displays a todolist.
# toDoApp = Tk()
# toDoApp.title("TodoListApp")
# toDoApp.configure(bg="blue")
# toDoApp.geometry("580x480")
# toDoApp.rowconfigure(0, minsize=50)
# toDoApp.columnconfigure([0, 1, 2, 3, 4], minsize=4)
# title_1 = Label(text="TO DO LIST", width=20, font=("bold", 30), bg="#9bd7e8")
# c1 = tk.Checkbutton(text='Do Dishes', onvalue=1, offvalue=0)
# c2 = tk.Checkbutton(text='Watch Tv', onvalue=1, offvalue=0)
# c3 = tk.Checkbutton(text='Do Yoga', onvalue=1, offvalue=0)

# title_1.grid(row=0, column=2)
# c1.grid(row=1, column=2)
# c2.grid(row=2, column=2)
# c3.grid(row=3, column=2)
# toDoApp.mainloop()

# Revision

# x = input()
# y = int(input())
# print(x * y)

# our_word = input("Please Enter a word: ")
# if our_word == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif our_word =="spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not ",  our_word, "!")

# income = float(input("Enter the annual income: "))
# Write your code here.
# if income > 0 <= 85528:
#     tax = income * 0.18 - 556.2
# if income > 85528:
#     surplus = income - 85528
#     out_tax = surplus * 0.32
#     tax = out_tax + 14839.2
# elif income > 1000 <= 85528:
#     tax = income * 0.18 - 556.2
# elif income <= 0:
#     tax = 0.0
# elif income > 0 <= 1000:
#     tax = 0.0
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# print(
#     """
#     +================================+
#     | Welcome to my game, muggle!    |
#     | Enter an integer number        |
#     | and guess what number I've     |
#     | picked for you.                |
#     | So, what is the secret number? |
#     +================================+
#     """)

# secret_number = 777
# our_number = int(input("Please enter a number: "))
# while our_number != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     our_number = int(input("Please enter a number: "))
# else:
#     print(our_number)
#     print("Well done, muggle! You are free now.")

# test_word = "chupacabra"

# while True:
#     question = input("Please enter a word: ")
#     if question == test_word:
#         break
# print("left the loop")

# Prompt the user to enter a word
# and assign it to the user_word variable.

# user_word = input("Please enter a word: ")
# user_word = user_word.upper()
# vowels = ['A', 'E', 'I', 'O', 'U']
# for letter in user_word:
#     if letter in vowels:
#         continue
#     print(letter)

# blocks = int(input("Enter the number of blocks: "))
# count = 0
# #
# # Write your code here.
# #
# while count < blocks:
#     height = blocks - 1
#     count += 1
#     print(height)


# print("The height of the pyramid:", height)

# step 1
# beatles = []
#
# print("Step 1:", beatles)
#
# # step 2
# beatles.append('John Lennon')
# beatles.append('Paul McCartney')
# beatles.append('George Harrison')
# print("Step 2:", beatles)

# # step 3
# for i in range(len(beatles)):
#     add_name = input("Please enter a name: ")
#     beatles.append(add_name)
#     print("Step 3:", beatles)
#     continue

# # step 4
# del beatles["Stu Sutcliffe'"]
# del beatles["Pete Best"]
# print("Step 4:", beatles)
#
# # step 5
# beatles.insert(0, "Ringo Starr")
# print("Step 5:", beatles)

# # testing list length
# print("The Fab", len(beatles))

# sorting with list

# my_list = [8, 10, 6, 2, 4, 88, 1, 12]
#
# swapped = True
#
# while swapped:
#     swapped = False  # no swaps
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
# m = [1,2,3]
#
# g = []
#
# for v in m:
#     g.insert(0,v)
# print
# i = 0
# while i <=5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("*")
# i = 0
# while i <= 3:
#     i +=2
#     print("*")
# m = [i for i in range(-1,2)]
# print(m)
# nums = [1,2,3]
# vals = nums[-1:-2]
# print(vals)
# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
# for i in range(1):
#     print("#")
# else:
#     print("#")
# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)

# def happ_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy new year")
#
# happ_new_year()

# def boring_func():
#     return 123
#
# x = boring_func()
#
# print("The boring function has returned its results ", x)

# def is_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
#
# a = float(input("Enter the first side\'s length: "))
# b = float(input("Enter the second side\'s length: "))
# c = float(input("Enter the third side\'s length: "))
#
# if is_triangle(a, b, c):
#     print("yes it can be a triangle")
# else:
#     print("It cant be a triangle")
#
#
# def is_right_angled_triangle(a, b, c):
#     if not is_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#
# # fibonacci numbers
#
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))
# # method 2
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# # Factorial number
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
#
#
# for n in range(1, 6):  # testing
#     print(n, factorial_function(n))
#
# # method 2
#
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)
#
# def fun(x):
#     x+= 1
#     return x
#
# x = 2
# x = fun(x + 1)
# print(x)
# m = (1,2,4,8)
# m = m[1:-1]
# m = m[0]
# print(m)
# def fun(x):
#     global y
#     y = x* x
#     return y
#
# fun(2)
# print(y)
# def f(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return  2
#
# print(f(f(2)))

# print(f(3))
# def alvin(x=0):
#     return x
#
# alvin(2)
# y = 3
# x = 6
# print(x + y)
# i = 0
# while i < i + 2:
#     i += 1
#     print("#")
# else:
#     print("#")
# def a(x):
#     return None
#
# def a_2(x):
#     return a(x) * a(x)
#
# print(a_2(2))
# m = [x * x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
# print(fun(m))

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x ,y-1)
#
#
# print(fun(0,3))

# def fun(x = 2, y = 3):
#     return x * y
#
# print(fun(y=2))

# dd = {}



