'''

1. Check your week 1 - week 2 notes for
Syntax, Runtime, and Logical errors
and identify them
2. What is unicode?
Convert a string into UTF-8 and print it
3. Write python code to print emojis
use any method you can find
* Bonus challenge *
- can you output emojis without imports?


'''


# Question 1

# Question 2

m = "Alvin".encode("utf-8")  # here i encode the str Alvin in variable n

print(m)

# here i decode the string

print(m.decode("utf-8", "backslashreplace"))

# Question 3

print("Hello sorry i cant be near you i have a cold", "\U0001F927","\U0001F927")


# Question 4

# this method we used CLDR "Common Local Data Repository"

def joke():
    ishappy = True
    if ishappy:
        print("John said Microsoft word is the best IDE for programmers ",
              "\N{rolling on the floor laughing}", "\N{rolling on the floor laughing}")


joke()




