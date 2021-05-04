'''
isPalandrome()

civic
dad

'''

p1 = "racecar"

p2 = "madam"

p3 = "hannah"


def isPalandrome(p):
    p = p.replace(" ", "")
    for i in range(len(p)):
        # here we reverse the word and compare it to the actual word and after check for the lengths of thw words
        if p[-i-1] == p[i]:
            return True


isPalandrome("hannah")
