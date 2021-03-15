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



