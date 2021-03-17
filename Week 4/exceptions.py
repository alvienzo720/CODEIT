# Scope
# variable in the global scope
greet = "Hello"

def hi():
    print(greet)

hi()

def sport():
    # variable in local scope
    fave = "basketball"

sport()
global = "Alvin"
def food():
    breakfast = "Toast"
    print(breakfast)

print(breakfast)

food()