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

cities = [['Kampala', 75.0], ['Newark', 30.0], ['Amsterdam', 50.0],
          ['Gulu', 80.0], ['Younde', 90.0], ['HongKong', 80.0],
          ['San Francicso', 60.0], ['Busan', 60.0]]

# 1 . print out all the items within the list
for city in cities:
    for one_city in city:
        print(type(one_city))
        print(one_city)

print("-----------------------------------------")
# 2. convert the temp from fareni to Celcius print the list
for city in cities:
    print(f"{city[0]} {city[1] - 32 * 5/9}")

# 3 add a second index value to each inner list(temp in Kelvins
print("-------------------------------------------")
for city in cities:
    city.append("kelvins")
    print(city)

