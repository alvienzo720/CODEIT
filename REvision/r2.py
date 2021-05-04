# l = [1, 2]
# for v in range(2):
#     v += 1
#     print(v)
#     l.insert(-1, l[v])
# print(l)

#
# nums = [1, 2, 3,5]
# print(len(nums))
# vals = nums
# print(len(vals))

#
# def fun(a, b):
#     return a ** b
#
# print(fun(2,b=2))

# z = 0
# y = 10
# x = y < z and z > y
# # print(x)
#
# m = y > z and z < y
# print(m)
# h = x or m
# print(h)

#Notes for references or and negation

# list_range = [x * x for x in range(5)]
# print(list_range)
# print(list_range[list_range[2]])
# print(list_range)
#
# def fun(l):
#     del l[l[2]]
#     return l
# Notes for reference

# a = 1
# b = 0
#
# a = a ^ b
# print(a)
# b = a ^ b
# print(b)
# a = a ^ b
# print(a)
# print(a,b)
# check more about bitwise operators

# a = 12
# print(~a)


# def fun(a, b , c=0):
#     print("Hello")
#
# # fun(a = 12 ,b=1)
# fun(a = 1, b= 0, c = 0)
#
# for i in range(-1,1):
#     print(i)
# i = 2
# while i >= 0:
#     print("*")
#     i-=2

# var = 0
# while var < 6:
#     var += 1
#    # print(var)
#     if var % 2 == 0:
#         continue
#     print("#")

# i = 0
# while i <= 5:
#     i += 1
#     print(i)
#     if i % 2 == 0:
#         break
#     print("*")

# nums = [3, 1, -2]
# print(nums[nums[-1]])

# nums = [[0,1,2,3] for i in range(2)]
# print(nums[2][0])

# var = 1
# while var < 10:
#     print("#")
#     var =  var << 1

# i = 0
# while i <= 3:
#     i +=2
#     print("*")

# counter = 5
# while counter > 3:
#     print(counter)
#     counter -= 1

# word = "Python"
#
# for letter in word:
#     print(letter, end="*")

# for i in range(1,100):
#     if i % 2 != 0:
#         print(i, end="-")
#
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end=" ")
#
# We use brea to exit the loop

# text = "pyxpyxpyx"

# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end=" ")
#
# continue is used to skip the currrent iteration and move to the next
#
# n = 0
#
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")

# for i in range(0,4):
#     print(i)
# else:
#     print(i, "else")

# for i in range(1,11):
#     if i % 2 != 0:
#         print(i, end="--")

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x, end="--")
#     x += 1

# email = "mutebialvinalvienzo@gmail.com"
#
# for ch in email:
#     if ch == "@":
#         break
#     print(ch, end=" ")

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# n = 3
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# n = range(4)
#
# for num in n:
#     print(num - 1)
# else:
#     print(num,"else")


# def nextSquare():
#     i = 1
#     while True:
#         yield i * i
#         i += 1

# for num in nextSquare():
#     if num > 100:
#         break
#     print(num, end="-")
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)

#
#
# x = 1
# y = 0
#
# a = x & y
# print(a)
# b = x | y
# print(b)
# c = ~x
# print(c)
# d = x ^ 5
# print(d)

# beatles = ["alvin", "hudson", "Mwasiti", "sharon"]
# for v in beatles:
#     print(v, end=" ")

# colors = ['red', 'green', 'orange']
#
# a = copy_whole_colors = colors[:] # copy the entire list
# b = copy_part_colors = colors[0:2]  # copy part of the list
#
# print(a)
# print()
# print(b)
#
# print()
# sample_list = ["A", "B", "C", "D", "E"]
# new_list = sample_list[2:-1]
# print(new_list)  # outputs: ['C', 'D']
# print()


list_1 = ["A", "B", "C"]
# # print(list_1)
# # list_2 = list_1
# # print(list_2)
# # list_3 = list_2
# # print(list_3)
# # del list_1[0]
# # del list_2
# # print(list_3)
# print(list_1)
#
# list_2 = list_1[:]
# print(list_2)
# del list_2[0]
# print(list_2)
# print(list_1[0:2])

# num = [num**2 for num in range(10)]
# print(num)

# board = [["alvin" for i in range(8)] for j in range(8)]
# print(board)

# temps = [[0.0 for h in range(24)] for d in range(31)]
#
# highest = -100.0
#
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
#
# print(highest)
#
#
# def hello(name):
#     print("Hello", name)
#
#
# name = input("Please enter your name: ")
#
#
# hello(name)

# def subtra(a, b):
#     print(a - b)
#
#
# subtra(5, b=2)
# subtra(2, b= 5)
#
# def add_numbers(a, b=2, c=0):
#     print(a + b + c)
#
# add_numbers(a=1,b=2, c= 3)

# def wishes():
#     print("My wishes")
#     return "Happy birthday"
#
# wishes()
# print()
# print(wishes())

# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list
#
#
# print(create_list(5))

# def hi():
#     return
#     print("hi")
#
#
# hi()

# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
#
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))

# a = 1
#
# def fun():
#     global a
#     a = 2
#     print(a)
#
# a = 3
# fun()
# print(a)


'''Recurssion'''


# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
#
# print(fun(25))


# Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
#
# # Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
#
# # Example 3
# tuple_3 = (1, 2, 3, 5)
# print(len(tuple_3))
#
# # Example 4
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 3
#
# print(tuple_4)
# print(tuple_5)



# pol_eng_dictionary = {
#     "kwiat": "flower",
#     "woda": "water",
#     "gleba": "soil"
#     }
#
# for key , value in pol_eng_dictionary.items():
#     print(key, "--", value)
#
# item_1 = pol_eng_dictionary["gleba"]    # ex. 1
# print(item_1)    # outputs: soil
#
# item_2 = pol_eng_dictionary.get("woda")
# print(item_2)    # outputs: water
#
# item_3 = pol_eng_dictionary.get("kwiat")
# print(item_3)
# pol_eng_dictionary["kwiat"] = "Air"
# print(pol_eng_dictionary["kwiat"])
# print(pol_eng_dictionary)


# scores = {
#     "alvin": 23
# }
# scores.update({"hudson": 22})
# scores.update({"mathew":90})
# scores.pop("alvin")
#
# print(scores)

#
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
#
# for item in (d1, d2):
#     d3.update(item)
#
# print(d3)

# colors = {
#     "white": (255, 255, 255),
#     "grey": (128, 128, 128),
#     "red": (255, 0, 0),
#     "green": (0, 128, 0)
#     }
#
# for m, a in colors.items():
#     print(m, ":", a)
# Bitwsie left shift
# x = 10 << 2
# m = 10
# print(x)
# # here we add 2 new 00 and it works for other numbers << ....2.3.4...
# print(bin(m))
#
# print(0b101000)

# nums = [1, 2, 3]
#
# vals = nums[:]
#
# print(len(vals))
# print(len(nums))
# print(hex(id(nums)))
# print(hex(id(vals)))


tup = (1, 2, 4, 8)
tup1 = (2,4)

m = tup[1] + tup1[1]

print(m)


