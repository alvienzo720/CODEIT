# cat = "meow"
# city = "Mewark"
# dog = "hound"
#
# def animanls():
#     print(cat)
#     global dog
#     dog = "woof"
#
#     def place():
#         print(city)
#
#     place()
#
#
# animanls()
# print(dog)
# #place()

# 1: Define a variable "dog" and give it a value "bark"

# 2: define a function called animal

# 3: define a global variable in the animal function called "dog" and set it to "woof"

# 4: after the function, call it

# 5: print dog
# Global Variable

dog = "bark"

def animal():
    global dog
    dog = "woof"

animal()
print(dog)


# UnboundLocalError

x = 0

def scope_prac():
    # locally bound x variable
    # x = 0
    x = x + 1
    print(x)

scope_prac()
