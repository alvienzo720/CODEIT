# 1: Define a set with the following values

'''

1,2,3,'a','b','c'

'''

# 2: define function called global_set

# 3: remove all numbers from the set

'''
'a','b','c'

'''

# 4: add a three new letter to the set

'''
'a','b','c','d','e','f'

'''

# 5: return the new set inside the function

# 6: call global_set and pass the set defined as a parameter

# 7: Print the set variable underneath the function call

a = {1, 2, 3, 'a', 'b', 'c'}


def global_set(m):
    m.remove(1)
    m.remove(2)
    m.remove(3)
    m.add("d")
    m.add("e")
    m.add("f")
    print(m)
    return m


global_set(a)
print(a)
