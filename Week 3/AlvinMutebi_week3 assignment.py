# 1.print out the word (num) amount of times

# 2.(Friday Challenge): print stars hills and diamonds

'''
Use a for loop and then a while loop for both:
input: 4
output:
*
**
****
***
**
*
Advanced Challenge
input: 5
output:
  *
 ***
*****
 ***
  *
'''

print("Question 1----------------")


def word_number_of_times():
    num = int(input("Please Enter a Number: "))

    word = input("Please Enter a word: ")

    count = 0

    while count < num:
        print(word)
        count += 1


word_number_of_times()


print("Question Two------------------")


def print_starts1():
    n = int(input("Please Enter a Number: "))
    for i in range(n):
        for m in range(i + 1):
            print("*", end="")
        print()
    for i in range(n):
        for m in range(i, n):
            print("*", end="")
        print()


print_starts1()

print("Question 3------------------")


def print_stars2():
    n = int(input("Please Enter a number: "))
    for i in range(n):
        for s in range(n, i+1, -1):
            print(end=" ")
        for j in range(i + 1):
            print(end="* ")
        print()
    for i in range(n):
        for s in range(i):
            print(end=" ")
        for j in range(i, n):
            print(end="* ")
        print()


print_stars2()