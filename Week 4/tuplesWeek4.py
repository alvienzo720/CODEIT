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


tup_c = 1, 2, 3, 4, 5

1# remove three

print(tup_c[:2] + tup_c[3:])

#print the tuple backwards

print(tup_c[::-1])
