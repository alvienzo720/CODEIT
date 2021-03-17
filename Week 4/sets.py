# sets : unordered , no duplicates

s = {1, "hi", 5.6}
print(s)  # printing sets

s = {1, "hi", 5.6, 5.6}
print(s)  # removes duplicates

# creating sets using set()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alpha_set = set(alphabet)
print(alpha_set, '\n')

# intializing an empty set

ex_set = set()

# adding to set
ex_set.add("name")
print(ex_set)

# set methodes

alpha_set.clear()
print(alpha_set)

# set diffrence

a = {'dog', 'cat', 'mouse'}
b = {'dog', 'bear', 'mouse'}

print(a.difference(b))
print(b.difference(a))

