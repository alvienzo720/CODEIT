# string indexing

day = "How was your day?"

print(day[0])  # first index is always Zero

print(len(day))

print(day[16])

print(day[-1])  # the last Indexs

print(day[:])

print(day[3:])  # stars from the third index and prints each other word

print(day[:10])  # here we consider (n-1) prints from zero index upto 9th index

print(day[4:10])  # prints from 4th index included to 10-1 upper bound(9th index)
'''
def replace(s,t,n):
    # string -s, target -t, new -n
        
    return

replace(x,y,z)
'''
# challenge
question = "How's your night so far?"

question = question[4:] + question[:]

print(question)


def str_replace(x, y, z):
    x = input("Input enter a sentence")
    y = input("Please enter a word to replace word")
    z = input("Please enter a target")
    for i in range(x):
        if x[i] == y:
            y = x[i]
            return y


str_replace("hello boys", "boys", "girls")

