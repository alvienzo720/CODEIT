'''
1. define a function called "String_Encoder":

takes parameters s with the following value

"It's a rainy day"

2. print the string backwards

3. replace "a" with "z"

4. return the encoded string
'''


# s = "I's a rainy day"
#
# a = (s[::-1])
# print(a)

def string_encode(s):
    a = ""
    for iterator in range(len(s)):
        #sprint(s[iterator])
        if s[-iterator-1] == "a":
            print("z")
        print(s[-iterator-1])




string_encode("Hello alvin")



