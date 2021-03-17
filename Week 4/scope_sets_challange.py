# 1.define two functions outer an inner

'''

nest inner function insode the outer function

'''

# 2. define a local variable "x" in the outer function

# 3. define a global variable "x" in the inner function

# 4. assign a string value "hello" to the local variable x in the outer function

# 5. assign a string value "goodbye" to the global variable x in the inner function

# 6. print(x) after the inner function, as the last line of the outer function

# 7. exit both functions and put a print(x) statement

# 8.

# 9. put a print(x) statement after function

# 10.define an x variable before the outer function

x = "see you later"


def outer():
    x = "Hello"

    def inner():
        global x
        x = "Goodbye"
    print(x)
    inner()


outer()
print(x)






