
# Arrays - lists (continued)

# list can order and values can be changed and repeated
person = ["Timmy", 10, 50.0, True]

print(person)

person.append("Allan")

#print(person)

# extends takes a list input and adds each value to an existing list
person.extend(["Ebong", 20, 10.0, False])
print(person)

person.remove('Ebong')
print(person)

person.insert(5, 'Dog')
print(person)

l2 = [2,4,5,7,32,143,3,6,5]
print(sorted(l2)) #sorted() takes a list parameters and returns a sorted list
