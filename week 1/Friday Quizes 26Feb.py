# print("#QUESTION 1")
#
# name = "Alvin Mutebi"
#
# print(name)
#
#
# print("#QUESTION 2")
# m = range(-10, -1)
# for i in m:
#     print(i)
#
#
# print("#QUESTION 3")
#
#
# def while_loop():
#     counter = -10
#     while counter < -1:
#         print(counter)
#         counter = counter + 1
#
#
# while_loop()
# print("#QUESTION 4")
#
#
# def hello():
#     print("hello world")
#
#
# hello()
#
#
# print("#QUESTION 5")
#
#
# def sum(x, y):
#     z = x + y
#     return z
#     print(sum(2, 4))
#
#     # print(z)
#     # when i use return z it dosent work for me
#
#
# print("#QUESTION 6")
#
#
# def odd_num():
#     for b in range(100):
#         if b % 2 != 0:
#             print(b)
#
#
# odd_num()
#
# print("#QUESTION 7")
#
#
# def isPrime(numb):
#     for i in range(2, numb):  # range of (numb-1) or nth
#         if numb % i == 0:
#             print(str(numb) + " Is NOT A Prime Number")
#             break
#     else:
#         print(str(numb) + " Is A Prime Number")
#
#
# isPrime(5)


def prime(n):
    for i in range(n):
        if i % 2 != 0:
            print(i)

# prime(100)
