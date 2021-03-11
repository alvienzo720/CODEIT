# for loops

day = "How is your day so far?"

for letter in day:
    print(letter)
    print(day.index(letter))

# nesting

num = 10

if num % 2 == 0:
    print("Even")
    if num % 5 == 0:
        print("Multiple of 5")
    else:
        print("even but not a multiple of 5")
else:
    print("num is not an even integer")



