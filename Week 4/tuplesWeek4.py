# array:Tuples
# they are inmutable
a_tup = (1, "Hello", 5.6, False)
b_tup = 'goodbye', True

print(type(a_tup))

# converting tuple to list
tup_list = list(a_tup)
print(type(tup_list))
print(tup_list)

# concatinating tuples

print(a_tup + b_tup)

# singleton tuple
sing_tup = ("single",)


# slicing tuples

print(a_tup[2:])

# removing tuples
first_item = a_tup
remove_hello = first_item + a_tup[2:]
print(remove_hello)


tup_c = 1, 2, 3, 4, 5, 5

# 1.remove three

print(tup_c[:2] + tup_c[3:])

# print the tuple backwards

print(tup_c[::-1])

# count how man items are in a tuple
print(len(tup_c))

# count how many times items appear in a tuple 5
print(tup_c.count(5))

# locate the index of a given item
print(tup_c.index(5))

# counting char in a string

fruit = 'banana'

count = 0

for letter in fruit:
    if letter == "a":
        count += 1
print(count)
print(fruit.count("a"))



