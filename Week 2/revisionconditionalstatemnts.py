# booleans

morning = True


night = False


# conditional statement


if morning:
    print("Good morning")


elif night:
    print("Its not the morning")


elif not night:
    print("It's night")

else:
    print("Its neither night or day")

print("------------------------------------")


# conditional statements 2

city = "Kampala"

if city == "Newark":
    print("Hi from New Jersey")
else:
    print("Its a city other than Newark")

print("------------------------------------")

age = 90

if age == 21:
    print("Your Ok")
elif age == 90:      # Else if , a specific condition
    print("Your lucky")
elif age < 21:
    print("Your too Young")
# any condition other than ones already accounted for
else:
    print("Not 21 not 90 bu grater than 21")

    