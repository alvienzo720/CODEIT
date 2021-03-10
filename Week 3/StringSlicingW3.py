# string indexing

# day = "How was your day?"
#
# print(day[0])  # first index is always Zero
#
# print(len(day))
#
# print(day[16])
#
# print(day[-1])  # the last Indexs
#
# print(day[:])
#
# print(day[3:])  # stars from the third index and prints each other word
#
# print(day[:10])  # here we consider (n-1) prints from zero index upto 9th index
#
# print(day[4:10])  # prints from 4th index included to 10-1 upper bound(9th index)
'''
def replace(s,t,n):
    # string -s, target -t, new -n
        
    return

replace(x,y,z)
'''


# challenge


def rep():
    question = "How's your night so far?"

    question = question[:11] + "day" + question[16:]

    print(question)


rep()

greeting = "How was your day today?"

a = greeting[:13]
b = greeting[16:-1]
c = "night"

print(a)
print(b)

f = f"{a}{c}"

print(f)


#
# def replace_func(s, t, n):
#     # string -s, target -t, new -n
#
#     return
#
#
# replace_func()


def is_palandrome(x, pos_index, neg_index):
    if x[pos_index] == x[neg_index]:
        print("")
    else:
        return False

    pos_index += 1
    neg_index -= 1

    is_palandrome(x, pos_index, neg_index)


print(is_palandrome("racecar", 0, -1))
