
#list
'''
list indexes can be counted like this
-3 -2 -1 0 1 2 
'''
days = ['mon', 'tues', 'wed', 'thurs',
        'fri', 'sat', 'sun']

print(days)

# accessing list elements

#prints the first item in the list 
monday = days[0]
print(monday)

wednesday = days[2]
print(wednesday)

# -1 is the last item in the list 
wednesday = days[-1]
print(wednesday)

# iterate through a list
print(len(days))

# method 1: iterating through a list 
for i in range(len(days)):
    print(days[i])

# method 2: iterating through a list without indices
for day in days:
    print(day+'day')



    
