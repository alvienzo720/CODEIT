class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello my name is ", self.name, "and iam ", self.age, "years old")


p = Person("alvin", 25)

p.hello()


class Reef:
    def brain_coral(self):
        print("brain coral is smooth")


class Plants(Reef):
    def moss(self, color):
        print("moss grows on rocks too")

