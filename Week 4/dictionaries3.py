employees = {'id': [201, 600],
             'name': ["Maximo", "Josephine"],
             'bonus': [1000, 2000]}

print(employees)

# 1: print out all the values of the dictionaries

m = employees.values()
print(m)

print(f"{employees['id']} {employees['name']} {employees['bonus']}")


# 2: print out all list values iteratively now

for key, value in employees.items():
    print(key, value)

# 3: add "locations" to the employees dictionary location:('USA', 'Uganda
employees.update({'location': ('USA', 'Uganda')})
print(employees)

# 4: Add a new entry into the dictionary the dictionary with new employee
# id -100
# name -"Hughey"
# bonus - 500
# location

employees['id'].append(100)
employees['name'].append('Hughey')
employees['bonus'].append(500)

# add the new location

print(employees['id'])
print(employees)
