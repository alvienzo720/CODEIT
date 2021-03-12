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
        if s[iterator] == "a":
            print("A is active")

            a = s[iterator::-1]

            print(a)


string_encode("Hello alvin")


def str_enc(s):
    e = ""
    for iterat in range(len(s)):
        if s[-iterat-1] == "a":
            e += "z"
            print('z')

        e += s[-iterat-1]
        print(e)
        print(s[-iterat-1])
    return e


str_enc("It's a raniny day")

# q = s[::-1].replace('a', 'z')

# print(q)