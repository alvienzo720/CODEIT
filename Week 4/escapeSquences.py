# Escape squenceies

# \t tab

print("Today was a raniny day \t it was cold too")

# \n new line
print("Today was a sunny day \n it was warm too")

# \b backspace charcter
print("Today is a cloudy day. \b We should get some rain")

# \
print("It\'s rainy outside \n")

# 'in' and 'not in operators

tup = ([1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e'])

# O(n)
for m in tup:
    if 'a' in m:
        print("Found a")
        break
    else:
        print("Could not find a")

# note in

# Tuple Challenge Day 3 Week $
# Tuple Challenge Day 2, week 4:

tup = ([1, 'a'], [2, 'b'], [4, 'd'], [5, 'e'])

# 1: add [3, 'c'] at index 2 using slicing
c = [3, 'c'],
tup = tup[:2] + c + tup[2:]

print(tup)

# 2: place this in a function called AddTuple


def Add2Tuple(c):
    integer = input("Enter an Integer: ")
    string = input("Enter a string")
    c = ([integer, string],)
    tup = ([1,'a'],[2,'b'],[4,'d'],[5,'e'])
    tup = tup[:2]+ c + tup[2:]
    return tup

single_tup = [3,'c'],

print(Add2Tuple(single_tup))


# 3: replace default values with user input



# add [3, 'c'] at index 2
