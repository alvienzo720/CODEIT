# sets are un indexed , unordered , unchangeable

a_set = {"apple", 4, "banana", "cherry", True}

print("apple" in a_set)

b_set = {"pear", 20, 4}

b_set.add(False)
print(b_set)

# return the union of sets without duplicated values

people = [('Ann', 30), ('Moses', 25), ('Elijah', 10), ('Dan', 40), ('Timothy', 15)]

print(type(people))

print(people[0][1])  # Not working for me

for person in people:
    print(person)
    if 'Moses' in person:
        print(f"{person[0]} is {person[1]} years old")
        break
print("------------------------")
if 'Moses' in person:
    print(f"{person[0]} is {person[1]} years old")
print("------------------------")

for i in range(len(people)):
    print(person)

print("------------------------")

for i in range(len(people)):
    print(people[i][:])

print("------------------------")
for i in range(len(people)):
    print(type(people[i][0]))

print("------------------------")

for i in range(len(people)):

    print(people[i][0], people[i][1])

'''
add a third element True to the tuples list "people"
'''


def tuple_list():
    for i in range(len(people)):
        print(people[i][:] + (True,))


tuple_list()


print("#solution two")


def list_tuple():  # issues
    for i in range(len(people)):
        p = people[i] + (True,)
        print(p)


list_tuple()

print("#method 3")


def one_liner():
    for i in range(len(people)):
        print(type(people[i] + (True,)))


one_liner()
