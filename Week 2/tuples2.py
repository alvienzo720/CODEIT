'''
TUPLES
tuples are ordered and unchangeable collections 
tuples allow dupliate values
'''
a_tuple = (1,2,3,4,5)

a_tuple = list(a_tuple)
#adding an item to the tuple
a_tuple.append(6)
a_tuple = tuple(a_tuple)

print(a_tuple)
#printing the data type 
print(type(a_tuple))

x_tuple = (10,11,12,13,14,15)
y_tuple = x_tuple[:2]
z_tuple = x_tuple[2:4]
#to print out 10 and 11
print(y_tuple)
#to print out 12 and 13
print(z_tuple)

single_tuple = (90,)
print(single_tuple)
'''
write a tuple and populate it with numbers 1-15
replace 5 with 'a'
remove 10 from the tuple
return the modified tuple


'''

def tu():
    
    m_tuple = (1,2,3,4,5,6,7,8,9,10,10,10,11,12)

    print(m_tuple[0:4] + ("a",) + m_tuple[5:])

    r_tuple = m_tuple[0:8] + r_tuple[11:]
    return r_tuple
tu()

one_liner():
     m_tuple = (1,2,3,4,5,6,7,8,9,10,10,10,11,12)
     return m_tuple[0:4] + 'a', + m_tuple[6:9] + m_tuple[11:]

oneliner()
    




tu()





