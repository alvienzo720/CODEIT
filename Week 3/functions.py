
def sum():
    x = 5
    y = 2
    print(x + y)

# run the function


sum()

# functions with parameters


def return_sum(a, b):
    return a + b


print(type(return_sum(2, 2)))

c = 5 + return_sum(2, 2)

print(c)

