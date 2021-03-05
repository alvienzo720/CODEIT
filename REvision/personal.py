# class and Instance Variables

class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []   # here we have an instance for each dog tricks

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fiddo')

e = Dog('Buddy')

e.add_trick('roll over')

d.add_trick('play dead')

q = Dog('Matt')

print(e.kind)

print(e.name)

print(d.name)

print(d.tricks)

print(e.tricks)

print(q.name)


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()

print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'

print(w2.purpose, w2.region)







