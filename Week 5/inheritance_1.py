import cars_main

A_Car = cars_main.Cars()

A_Car.model = "Honda"
A_Car.year = 2018
A_Car.color = "Red"

print(A_Car)
print(A_Car.model)
print(A_Car.year)
print(A_Car.color)

B_Car = cars_main.Cars()

B_Car.model = "Suzuki"
B_Car.year = 2019
B_Car.color = "Blue"

print(B_Car.model)
print(B_Car.year)
print(B_Car.color)

C_Car = cars_main.Cars()

C_Car.model = "Lamborghini"
C_Car.year = 2020
C_Car.color = "Yellow"

print(C_Car.model)
print(C_Car.year)
print(C_Car.color)



def ex():
    c = "c"
    print(c)
    def mid():
        global b
        b = "b"
    mid()
    print(b)
    def inner():
        global a
        a = "a"
    inner()
    print(a)



ex()