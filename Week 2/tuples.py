# TUPLES
# Tuples are immutable
a_tuple = (1, 2, 3)


print(a_tuple)

b_tuple = a_tuple + (4, 5, 6)

print(b_tuple)

# slice to form new tuples
c_tuple = b_tuple[2:]
print(c_tuple)

name = "Mutebi"
age = 100
happy = True

info = (name, age, happy)

print(info)

l = ['a', 'b', 'c']

l.append('e')

l = tuple(l)

print(l)
