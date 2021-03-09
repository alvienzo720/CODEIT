# import sys
# sys.setrecursionlimit(100)


def loop(x):
    print(x)
    x -= 1
    #print(x)
    loop(x)


#loop(100)


# def greet():
#     i = 0
#     if 10 > i >= 0:
#         print("Hello")
#     greet()
#
# greet()

def recursive_loop(x):
    if x > 99:  # BASE CASE
        return

    print(x)
    x = x + 1

    recursive_loop(x)


recursive_loop(2)
