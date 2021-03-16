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

for m in tup:
    if 'a' in m:
        print("Found a")
        break
    else:
        print("Could not find a")

